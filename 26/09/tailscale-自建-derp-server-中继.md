---
title: "tailscale 自建 derp server 中继"
date: 2026-09-28 21:09:32
tags: ["26", "09"]
author: "deepseek 41 flash"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

by: deepseek 41 flash. verified ok.

see: https://ameow.xyz/archives/tailscale-derp-server-deployment

# 阿里云自建 Tailscale DERP 中继

**服务器** （Ubuntu 22.04） · **区域** `900 / gz / Guangzhou` ·
**端口** `TCP 13477`（DERP）、`UDP 13478`（STUN）

最终效果：`tailscale netcheck` → `Nearest DERP: Guangzhou (17.7ms)`，全 tailnet 客户端自动选它作为 home DERP。

---

## 1. 服务端：修复 DNS（前置条件）

阿里云这台机器 DNS 完全不可用：`127.0.0.53` 存根本身超时，DHCP 下发的 `100.100.2.136/138` 也不通 —— 表现为**任何域名都解析不了**，与 Docker/镜像源无关。

```bash
# /etc/netplan/50-cloud-init.yaml
network:
    version: 2
    ethernets:
        eth0:
            dhcp4: true
            dhcp4-overrides: { use-dns: false }
            nameservers: { addresses: [223.5.5.5, 119.29.29.29] }

# /etc/systemd/resolved.conf
[Resolve]
DNS=223.5.5.5 119.29.29.29
FallbackDNS=223.6.6.6 180.76.76.76

# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg —— 阻止 cloud-init 回滚
network: {config: disabled}
```

```bash
sudo netplan generate && sudo netplan apply
sudo systemctl restart systemd-resolved
```

> ⚠️ 注意 `registry-1.docker.io` 在国内被投毒到 `2a03:2880:...:face:b00c::`（Facebook 段），Docker Hub 必须走镜像源。

## 2. 服务端：Docker 镜像源

```bash
# /etc/docker/daemon.json
{ "registry-mirrors": [
    "https://docker.m.daocloud.io",
    "https://docker.1ms.run",
    "https://docker.xuanyuan.me" ] }
```

```bash
sudo systemctl restart docker
```

## 3. 服务端：启动 derper

`ghcr.io` 在国内直连不稳，用南大镜像站拉取后重打 tag：

```bash
docker pull ghcr.nju.edu.cn/yangchuansheng/ip_derper:latest
docker tag ghcr.nju.edu.cn/yangchuansheng/ip_derper:latest \
           ghcr.io/yangchuansheng/ip_derper:latest
```

**`~/services/tailscale/docker-compose.yml`**

```yaml
services:
  derper:
    image: ghcr.io/yangchuansheng/ip_derper
    container_name: derper
    restart: always
    environment:
      - DERP_ADDR=:13477
      - DERP_VERIFY_CLIENTS=true      # 走宿主 tailscaled 校验客户端身份
    ports:
      - "13477:13477"
      - "13478:3478/udp"
    volumes:
      - /var/run/tailscale:/var/run/tailscale   # 挂目录，不是单个 socket 文件
```

```bash
cd ~/services/tailscale && docker compose up -d
```

本机是 tailnet 节点（DERP 校验身份需要宿主跑着 tailscaled 并已登录）。

## 4. 服务端：修 tailscaled 重启导致容器失联的坑

**根因**：systemd 的 `RuntimeDirectory=tailscale` 会在 tailscaled 每次重启时**删除并重建整个 `/run/tailscale` 目录**。容器里无论挂单文件还是挂目录，bind mount 都会指向被删除的旧 inode → `dial unix ...: connection refused` → derper 把所有客户端 `rejected` → DERP 连上就 `EOF`。

```bash
sudo mkdir -p /etc/systemd/system/tailscaled.service.d
# /etc/systemd/system/tailscaled.service.d/derper.conf
[Service]
RuntimeDirectoryPreserve=yes   # systemd 永不删除该目录，容器无需重启即可看到新 socket
```

```bash
sudo systemctl daemon-reload && sudo systemctl restart tailscaled
```

## 5. 服务端：安全组

阿里云 ECS → 安全组 → 入方向，两条规则（源 `0.0.0.0/0`）：

| 协议 | 端口 |
|---|---|
| 自定义 TCP | `13477/13477` |
| 自定义 UDP | `13478/13478` |

主机侧 `ufw`/`firewalld` 均 inactive，无需额外配置。
> 服务器上 `curl` 自己的公网 IP 会失败，是阿里云 1:1 NAT 不支持回环，**正常现象**。

---

## 6. Tailscale ACL

`https://login.tailscale.com/admin/acls/file`（可视化 Policies 页不显示 `derpMap`），加一个与 `grants`/`acls` **同级**的顶层键：

```json
"derpMap": {
  "OmitDefaultRegions": false,
  "Regions": {
    "900": {
      "RegionID": 900,
      "RegionCode": "gz",
      "RegionName": "Guangzhou",
      "Nodes": [{
        "Name": "aliyun-derper",
        "RegionID": 900,
        "HostName": "47.103.61.134",
        "IPv4": "47.103.61.134",
        "DERPPort": 13477,
        "STUNPort": 13478,
        "CanPort80": false,
        "InsecureForTests": true
      }]
    }
  }
}
```

各字段的必要性：

| 字段 | 为什么 |
|---|---|
| `STUNPort` | **不能省**。省略时 netcheck 默认探 `3478`（未开放）→ 测不到延迟 → 区域永不被选中 |
| `InsecureForTests` | 容器自签证书 CN/SAN 是 `127.0.0.1`，靠它跳过域名校验 |
| `IPv4` | 让客户端直接连 IPv4，避免 DNS 解析 |

保存后客户端需重新拉取 netmap（退出重开 Tailscale.app）。

---

## 7. 验证

```bash
# 服务端
sudo tailscale debug derp gz          # 应显示 Region 900 == "gz"
tailscale netcheck                    # 出现 gz 及低延迟
curl -k -i -N -H "Connection: Upgrade" -H "Upgrade: DERP" \
     https://47.103.61.134:13477/derp  # 期望 HTTP/1.1 101 Switching Protocols

# 客户端
tailscale ping <peer>                 # 期望 pong ... via DERP(gz)
tailscale status                      # peer 后显示 relay "gz"
```

---

## 8. 三个「假警报」，看到不用管

1. **`tailscale debug derp` 报 `x509: certificate signed by unknown authority`**
   该命令自身的 bug：`ipn/localapi/debugderp.go` 的 `tlsConfigForNode()` 漏了 `InsecureForTests`（只处理 `CertName`）。
   真正建连的 `derphttp.tlsClient()` 是认这个字段的，中继不受影响。

2. **`is port 80 blocked?`**
   `CanPort80: false` 且安全组本来就没开 80，正常。

3. **标准 STUN 探包无响应**
   Tailscale 的 derper STUN 用私有方言：只回应带 `SOFTWARE="tailnode"` **且**以合法 `FINGERPRINT`（`crc32 ^ 0x5354554e`）结尾的请求，其余静默丢弃（`ErrWrongSoftware`）。
   用 `stun.miwifi.com` 之类公网 STUN 能通、用你的 derper 不通，**不代表 derper 坏了**。

   ```python
   import struct, os, zlib
   software = b"tailnode"
   tid = os.urandom(12)
   attr = struct.pack('>HH', 0x8022, len(software)) + software
   msg = struct.pack('>HH', 0x0001, len(attr) + 8) + b'\x21\x12\xa4\x42' + tid + attr
   msg += struct.pack('>HHI', 0x8028, 4, zlib.crc32(msg) ^ 0x5354554e)
   ```

---

## 9. 已知限制

- **无法强制「只走 DERP」**：Tailscale 始终优先点对点直连，DERP 只是兜底。`tailscale set/up` 没有相关开关。
- **DERP 区域选取是自动的**：由 netcheck 挑延迟最低的区域，无需手动指定。
- **STUN 是区域被选中的必要条件**（不是可选项）：UDP 可用时，netcheck 只用 STUN 测延迟；HTTPS/ICMP 兜底仅在**所有** STUN 探测都失败时才触发。

## 10. 日常运维

```bash
cd ~/services/tailscale
docker compose ps / logs -f derper / restart / up -d
```

| 项 | 值 |
|---|---|
| 容器 | `restart: always` |
| docker | `systemctl enable` 已开 |
| tailscaled 重启 | derper 无需重启（`RuntimeDirectoryPreserve=yes`） |


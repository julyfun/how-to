- reliability: "20% (author)"
- date: 2024-10-29
- os: "macos 14.5, wsl2 ubuntu 22.04, win11"
- author: "Julyfun MacOS14.5 M1"
- assume-you-know: [computer]

# Build your zerotier LAN for mac, win and wsl

- Basic tutorial : https://github.com/xubiaolin/docker-zerotier-planet
    - `200 Join OK` on windows but windows is not listed in webui?
        - Double check the Port you selected when `./deploy.sh` is allows in your server security group!
        - Make sure you've `Easy Setup` the ip range (like in tutorial) (Don't make the ip range look like your ethernet)

## wsl2 special part

- For wsl2, if `zerotier join` completely failed and show `cannot bind to local control interface port 9993` in zerotier-one's log:
    - Make sure this in `wslconfig`, this is necessary (ref: perplexity):

```
[boot]
systemd=true
```

- For wsl2, also make sure `/etc/ssh/sshd_config` looks like this:

```
Port 2222 # winows22端口另有他用,改为2222,避免冲突
ListenAddress 0.0.0.0        # 如果需要指定监听的IP则去除最左侧的井号，并配置对应IP，默认即监听PC所有IP
PermitRootLogin yes # 如果你需要用 root 直接登录系统则此处改为 yes
PasswordAuthentication yes    # 将 no 改为 yes 表示使用帐号密码方式登录
AllowTcpForwarding yes
AllowUsers *
```

- (Maybe necessary) Allow 2222 port in windows firewall rule settings.
- ssh like this: `ssh julyfun@10.81.23.35 -p 2222`
- Success!

## Problems

- Can't ping wsl2 though webui show all devices are ONLINE?
    - Try pinging from each other (win, wsl, mac)
    - Do nothing and wait.
    - Done!


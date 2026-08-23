---
title: "RoboDojo"
date: 2025-08-23 08:16:17
tags: ["工作", "sim"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

# RoboDojo 配置与 Pi0 微调/评测指南

本文分为通用配置方法，以及本次 RTX 4090/570 驱动/Isaac Sim 5.1 环境的特定问题。

## 一、通用配置方法

### 1. 版本、路径和系统依赖
- 官方文档：https://robodojo-benchmark.com/doc/usage/install-and-download/
- 记录 RoboDojo commit、Isaac Sim/Lab、PyTorch、JAX、CUDA 版本；严格使用锁定版本，不主动升级。
- 全新机器不要复用旧 conda/uv 环境；大文件放共享盘，不放 home 或 root。
- 安装 git-lfs、编译工具、ffmpeg、Vulkan、libGL/libEGL/libGLU/libXt 等系统依赖；先检查 nvidia-smi、df -h、free -h。

### 2. 镜像、代码和 RoboDojo 环境
建议设置 HF_ENDPOINT=https://hf-mirror.com、HF_HUB_ENABLE_HF_TRANSFER=1、HF_HOME、PIP/UV 镜像及较大的下载 timeout。镜像只影响下载，不改变代码版本。
使用官方仓库及 submodule：git clone --recurse-submodules；运行 scripts/robodojo.sh --help、install、doctor。不要自行拼装 Isaac 依赖。
本次 conda 激活：source /inspire/hdd/project/robot-reasoning/xiangyushun-p-xiangyushun/mingzhu/miniconda3/etc/profile.d/conda.sh && conda activate RoboDojo。

### 3. Assets、Vulkan 和最小仿真
严格用官方脚本下载 Assets；用 find -L 检查软链接目标，du -sh 检查大小。先运行 vulkaninfo --summary，再运行最小 headless 仿真。
必须确认 app ready、场景创建、reset、至少一个 step 和正常退出；不要一开始跑全部 layout。

### 4. Pi0/openpi、数据和微调
按 Pi_0 README 和锁文件用 uv 创建 openpi 环境，不手动升级依赖；用 openpi/.venv/bin/python -c 'import jax; print(jax.devices())' 验证 CUDA。
Policy server 使用 Pi0 uv；Isaac/eval client 使用 RoboDojo conda，不能混用。
先确认第一个任务、数据配置和官方 checkpoint 名称，只下载该任务所需数据与权重并记录路径、大小、校验信息。
微调不需要 Isaac Sim graphics，只需要训练数据、Pi0 uv 和 GPU。显存不足优先降低 batch size、梯度累积或 gradient checkpointing；多 GPU 时明确 CUDA_VISIBLE_DEVICES 和每进程 GPU。

### 5. 评测顺序和结果核验
先 eval_num=1，确认 server 加载、WebSocket connected、reset、实际 step 和最新 _result.json，再改为 10。
结果必须同时核对最新 _result.json、Success nums、Fail nums、Unstable nums；不要使用旧日志行推断新结果。
长任务使用 nohup，记录 PID、timeout、日志和显存。SSH 断开不等于后台进程停止。

### 6. GPU burn
评测期间不要运行 gpu_burn.py；评测完全退出且显存释放后再运行。空闲命令：
nohup /inspire/.../miniconda3/envs/RoboDojo/bin/python /inspire/.../mingzhu/gpu_burn.py 50 >/tmp/robodojo_gpu_burn.log 2>&1 </dev/null &
记录 PID 到 /tmp/robodojo_gpu_burn.pid；停止时按准确 PID 操作，不要宽泛 pkill -f python。

## 二、本次环境的特定问题

### 1. 实际环境
机器 lmz-fastwam5；RTX 4090；驱动 570.124.06；Isaac Sim 5.1.0.0；Isaac Lab 0.54.3；Torch 2.7.0+cu128。
RoboDojo conda：
Pi0 uv：

### 2. 显卡、驱动和系统库
fastwam4 的 595.58.03 在 Isaac Sim 5.1 的 librtx.scenedb.plugin.so 阶段段错误；官方 5.1 文档列出的 Linux 验证驱动为 580.65.06，论坛也有 595/Vulkan 崩溃案例。
改用 fastwam5 的 570 后可到 app ready，完成渲染、场景创建和 rollout，无需更换 Isaac Sim 版本。570 未列入官方验证范围，但在本机实际可用。
fastwam5 初始缺少 libXt.so.6、libGLU.so.1；安装 sudo apt-get install -y libxt6 libglu1-mesa。

### 3. Vulkan ICD
nvidia-smi 不能代表 Vulkan 枚举；CUDA_VISIBLE_DEVICES 不能选择 Vulkan GPU；重复 ICD 可能导致错误枚举。
本次启动时限定：VK_ICD_FILENAMES=/etc/vulkan/icd.d/nvidia_icd.json、DISABLE_LAYER_NV_OPTIMUS_1=1、DISABLE_LAYER_NV_PRESENT_1=1、ROBODOJO_PRESERVE_CUDA_VISIBLE_DEVICES=1。
不要未经确认删除系统 ICD 文件；用 vulkaninfo 和 Isaac 日志判断。

### 4. 两个代码兼容问题
CPU annotator 可能返回 numpy.ndarray，而相机批处理假定 Warp .device；camera_view.py 已增加 ndarray 到 CPU Warp array 转换。
旧 checkpoint norm stats 使用 observation.state/action，Pi0 adapter 使用 state/actions，会报 Selector key observation.state not found in tree。model.py 已将 observation.state 映射为 state、action 映射为 actions。
遇到 selector key 错误，先比较 checkpoint schema 和 adapter 输入树，不要盲目重新下载。

### 5. WebSocket 超时
websockets 默认每 20 秒 Ping 并要求 20 秒 Pong；Pi0 推理阻塞 event loop 时会出现 keepalive ping timeout 和 RECONNECT。
本次 client/server 的 ws_ping_timeout_s 改为 None：保留 Ping keepalive，但不因推理长延迟断线。单回合验证中重连从正式评测期间的频繁发生降为仅 1 次。这改善通信，不会自动提高策略成功率。

### 6. 本次正式结果
任务 arrange_largest_number；env_cfg arx_x5；action joint；checkpoint RoboDojo-arrange_largest_number_ft1-arx_x5-joint-0。
正式 10 回合：Success 0、Fail 10、Unstable 0、score 0.0、success_rate 0.0。
结论：仿真、渲染、Pi0 推理、通信和评测链路已打通；0/10 是当前 checkpoint 的策略表现，不是 Isaac Sim 启动失败。

### 7. 本次代码修改清单
1. camera_view.py：CPU annotator ndarray 兼容。
2. XPolicyLab/policy/Pi_0/model.py：旧 norm stats key 兼容。
3. XPolicyLab/client_server/ws/protocol/client.py：ping_timeout=None。
4. XPolicyLab/client_server/ws/model_server.py：ping_timeout=None。

## 三、易错点速查
1. Pi0 uv 与 RoboDojo conda 不能混用。
2. 不要只看 nvidia-smi 判断 Vulkan GPU。
3. 评测时不要同时运行 gpu_burn.py。
4. 结果按最新 _result.json 修改时间核对。
5. WebSocket timeout 不等于 Isaac Sim 崩溃。
6. 启动错误先查 .so、ICD、驱动和缓存，再考虑重装。
7. 先第一个任务、eval_num=1，再正式 10 回合。
8. 共享盘满载时不要重复启动多个 server。
9. SSH 断开后先查后台 PID，不要重复启动。
10. 评测完成后再直接启动 GPU burn。

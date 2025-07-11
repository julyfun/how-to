---
title: 3D-Diffusion-Policy
date: 2025-04-24 18:23:11
tags: ["notes", "julyfun", "25", "policy"]
---
- 符号
    - `T`: 预测轨迹长度
- `eval_policy.py` 调用 `deploy_policy.py:eval()`，其调用 `RobotRunner.get_action()`
- `RobotRunner.get_action()` (robot_runner.py)
    - `obs = self.get_n_steps_obs()`
        - obs <- update_obs() 就是 append <- Base_task.get_obs()
            - [ai]
            - **observation** - 包含来自各种相机的观察数据
               - 相机数据包括 `head_camera`, `left_camera`, `right_camera`, `front_camera` 等
               - 每个相机可以包含以下数据（取决于 `data_type` 设置）：
                 - `rgb` - RGB图像数据
                 - `mesh_segmentation` - 网格分割数据
                 - `actor_segmentation` - 实体分割数据
                 - `depth` - 深度图像数据
                 - 相机内参和外参矩阵
            - **pointcloud** - 点云数据
               - 如果 `data_type['pointcloud']` 为 True，则包含点云数据
               - 可以选择是否合并多个相机的点云数据
            - **joint_action** - 机器人关节状态
               - 如果 `data_type['qpos']` 为 True，包含机器人关节角度
               - 双臂模式下，包含左臂和右臂的关节角度
               - 单臂模式下，仅包含右臂的关节角度
            - **endpose** - 机器人末端执行器姿态
               - 如果 `data_type['endpose']` 为 True，包含末端执行器的位置和姿态
               - 双臂模式下，包含左右两个末端执行器的信息（位置x,y,z，欧拉角roll,pitch,yaw，以及夹爪状态）
               - 单臂模式下，仅包含右臂末端执行器信息
            - **vision_tactile** - 视觉触觉传感器数据（当 `TACTILE_ON` 为 True 时）
               - 如果 `data_type['vision_tactile']` 为 True，包含触觉传感器的RGB图像数据
        - 随后拿出两个数据并重命名: pointcloud -> point_cloud, joint_action -> agent_pos
        - 得到 obs: `Dict`
            - each_key => 将最近 n 个观测的 key 在第 0 维度拼接. 形状为 `(n_steps, ) + shape_of_the_value`
                - n_steps 在参数 yaml 里为 n_obs_steps = 3
        - 在前面 unsqueeze 一个长度为 1 的维度后送进 `DP3.predict_action()` （应该是因为推理的时候 batch 必是 1）

```python
class DP3:
    predict_action() and  (dp3.py)
        [arg] (obs_dict):
            'point_cloud': (1, 3, 1024, 6)
            'agent_pos': (3, 14) 就是关节角度

        normalize()
        if @?global_cond:
            point_cloud & agent_pos 都送入 DP3Encoder，得到 (3, 192)，压扁成 (1, 576)
            mask 就是全部 mask 掉, 所有动作都需要通过扩散模型生成
        else:
            mask 观察特征保持可见
            送入 self.condition_sapmle()
            return. 实测表明一次预测 6 步且会把这 6 步执行完，再预测下 6 步.

    condition_sample():
        生成的 traj shape 是 (B, T, action_dim) = (1, 8, 14)
        每个去噪步 model(sample=trajectory, timestep=t, local_cond=local_cond(必为 None), global_cond=global_cond)
        model is @ConditionalUnet1D.forward():
```

```python
[ConditionalUnet1D.forward()]:
    ...

    timestep: (形状 (B, ) or int)
    encoding: (SinusoidalPosEmb, Linear, Mish, Linear)

    if global_cond: global_feature = cat([timestep_embed, global_cond], axis=-1) }

    [Downsample]
    x = sample (生成 trajactory)
    for idx, (@resnet, @resnet2, @downsample) in enumerate(self.down_modules):
        if self.use_down_condition:
            x = resnet(x, global_feature)
            if idx == 0 and len(h_local) > 0:
                x = x + h_local[0]
            x = resnet2(x, global_feature)
        else:
            x = resnet(x)
            if idx == 0 and len(h_local) > 0:
                x = x + h_local[0]
            x = resnet2(x)
        h.append(x)
        x = downsample(x)

    [mid_module (@ConditionalResidualBlock1D)]
    ...

    [Upsample]
    对称的

    [return]
    x = self.final_conv(x)
    return x

[resnet] = @ConditionalResidualBlock1D(
    dim_in, dim_out, cond_dim=cond_dim,
    kernel_size=kernel_size, n_groups=n_groups,
    condition_type=condition_type
),
[resnet2] = ConditionalResidualBlock1D(
    dim_out, dim_out, cond_dim=cond_dim,
    kernel_size=kernel_size, n_groups=n_groups,
    condition_type=condition_type
),
[downsample] = Downsample1d(dim_out) if not is_last else nn.Identity()

[ConditionalResidualBlock1D].forward():
    out = Conv1dBlock() (x)
    if `cross_attention_add`
        embed = CrossAttention() (x)
        out = out + embed (是 tensor 值加)
    out = another Conv1dBlock() (x)
    out = out + self.residual_conv(x)
    return out
```

```python
DP3Encoder:
    'point_cloud' => B x N x 3的 点云 (B: batch) = (3, 1024, 3) 送入 PointNetEncoderXYZ:

class PointNetEncoderXYZ
    MLP: [Linear + LayerNorm + ReLU] x 3
         channels: 3 => 64 => 128 => 256 => max => Linear + LayerNorm (128)

    forward():
        (B, N, 3) = (3, 1024, 3)
        mlp => (3, 1024, 256)
        max => (3, 256)
        Linear + LayerNorm => (3, 128)
        self.state_mlp: 简单的 MLP (Linear + ReLU). state_mlp_size = (64, 64).
        最后 cat 成 (3, 192)
 ```


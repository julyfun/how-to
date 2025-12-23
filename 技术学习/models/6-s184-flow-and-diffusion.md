---
title: MIT 6.S184 Flow and diffusion
date: 2025-11-10 00:39:48
tags:
  - notes
  - julyfun
  - 技术学习
  - models
author: julyfun-4070s-ubuntu2204
os: "Linux julyfun-4070s-ubuntu 6.8.0-87-generic #88~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct 14 14:03:14 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know:
  - computer
confidence: 2
---
- ODE（常微分方程） SDE（随机微分方程, 带随机波动的变化）
- SDE: 系统的未来状态不仅依赖当前状态，还包含非决定性的随机波动（噪声），因此未来状态是一个概率分布. 方程中多了随机项（通常用布朗运动表示）
- CFM: ?
- 教材笔记，详实简单: https://arxiv.org/pdf/2506.02070
- Lab: https://github.com/eje24/iap-diffusion-labs
## Lec 1
- https://diffusion.csail.mit.edu/docs/slides_lecture_1.pdf
- Diffusion network 预测的就是向量场（输入: t, X 当前位置. 输出: X 速度）
![Screenshot from 2025-11-10 01-25-29.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-toScreenshot%20from%202025-11-10%2001-25-29.png)
- 改为神经网络形式（引入 $theta$）. 注意这里 $sigma_t$ 可以由时间变化:
- ![Screenshot from 2025-11-10 01-24-27.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-toScreenshot%20from%202025-11-10%2001-24-27.png)
- [qm] 为何噪声到图像的过程可以建模为带布朗运动的 SDE?

## Lec 2
- Conditional Probability Path: 给定目标点 $z$（例如 diffusion 中的最终图像），求 $x$ 下一步路径
- Marginal Probability Path: 不给定条件（所有分布的加权平均），求下一步路径
	- 两者在 $t_0$ 是完全一样的，从第二步开始才有区别.
- 向量场函数（也可视为梯度或者速度）：$$"def" u(x: RR^d, t: [0, 1]) |-> RR^d$$
- ![image.png|700](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20251111103019.webp)
- [qm] 为何 score function 这样定义


[附]
- 很好的散度讲解: https://zhuanlan.zhihu.com/p/165479232kj

## Lec3 ok

## Lec4: Guided (conditional) DDM
- https://github.com/eje24/iap-diffusion-labs/blob/main/solutions/lab_three_complete.ipynb
- condition 是怎么加入 UNet: 自己看代码无需多言.
- ![截屏2025-11-11 11.10.16.png|700](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/%E6%88%AA%E5%B1%8F2025-11-11%2011.10.16.webp)

```python
class ResidualLayer(nn.Module):
    def __init__(self, channels: int, time_embed_dim: int, y_embed_dim: int):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.SiLU(),
            nn.BatchNorm2d(channels),
            nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        )
        self.block2 = nn.Sequential(
            nn.SiLU(),
            nn.BatchNorm2d(channels),
            nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        )
        # Converts (bs, time_embed_dim) -> (bs, channels)
        self.time_adapter = nn.Sequential(
            nn.Linear(time_embed_dim, time_embed_dim),
            nn.SiLU(),
            nn.Linear(time_embed_dim, channels)
        )
        # Converts (bs, y_embed_dim) -> (bs, channels)
        self.y_adapter = nn.Sequential(
            nn.Linear(y_embed_dim, y_embed_dim),
            nn.SiLU(),
            nn.Linear(y_embed_dim, channels)
        )
        
    def forward(self, x: torch.Tensor, t_embed: torch.Tensor, y_embed: torch.Tensor) -> torch.Tensor:
        """
        Args:
        - x: (bs, c, h, w)
        - t_embed: (bs, t_embed_dim)
        - y_embed: (bs, y_embed_dim)
        """
        res = x.clone() # (bs, c, h, w)

        # Initial conv block
        x = self.block1(x) # (bs, c, h, w)

        # Add time embedding
        t_embed = self.time_adapter(t_embed).unsqueeze(-1).unsqueeze(-1) # (bs, c, 1, 1)
        x = x + t_embed

        # Add y embedding (conditional embedding)
        y_embed = self.y_adapter(y_embed).unsqueeze(-1).unsqueeze(-1) # (bs, c, 1, 1)
        x = x + y_embed

        # Second conv block
        x = self.block2(x) # (bs, c, h, w)

        # Add back residual
        x = x + res # (bs, c, h, w)
```
不禁令人发现：
- 自然语言适合描述低频信号，而不擅长描述高频信号
- UNet 通过保留高频信号来抑制信息过于平滑的问题
- 之所以“*视频能展示的内容远少于占用空间相同的游戏*"是因为 mp4 需要编码高频信号
- AE 压缩为低维**潜在向量**的结构之所以能用于生成，是因为它强制学习数据的底层结构

Some question
- 这里如何编码时间 (bs, 1, 1, 1) => (bs, emb_dim)？用了 nn.Parameter.
- 可能也可以用无需学习的正弦余弦位置编码
```python
class FourierEncoder(nn.Module):
    """
    Based on https://github.com/lucidrains/denoising-diffusion-pytorch/blob/main/denoising_diffusion_pytorch/karras_unet.py#L183
    """
    def __init__(self, dim: int):
        super().__init__()
        assert dim % 2 == 0
        self.half_dim = dim // 2
        self.weights = nn.Parameter(torch.randn(1, self.half_dim))

    def forward(self, t: torch.Tensor) -> torch.Tensor:
        """
        Args:
        - t: (bs, 1, 1, 1)
        Returns:
        - embeddings: (bs, dim)
        """
        t = t.view(-1, 1) # (bs, 1)
        freqs = t * self.weights * 2 * math.pi # (bs, half_dim)
        sin_embed = torch.sin(freqs) # (bs, half_dim)
        cos_embed = torch.cos(freqs) # (bs, half_dim)
        return torch.cat([sin_embed, cos_embed], dim=-1) * math.sqrt(2) # (bs, dim)
```
- ![截屏2025-11-12 08.13.03.png|700](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/%E6%88%AA%E5%B1%8F2025-11-12%2008.13.03.webp)

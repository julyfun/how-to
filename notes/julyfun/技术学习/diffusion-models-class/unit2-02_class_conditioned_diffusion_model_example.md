---
title: unit2-02_class_conditioned_diffusion_model_example
date: 2025-06-10 01:55:37
tags: ["notes", "julyfun", "技术学习", "diffusion-models-class"]
---
## Class-conditioned

指的是类别-Conditioned. 或者说 class-label-conditioned.

## 网络输入改成啥样了? 其实就是 concat.

- Unet 输入通道直接改成了 `in_channels=1 + class_emb_size`
```python
UNet2DModel(
    in_channels=1 + class_emb_size,
```

- forward 时广播 + torch.cat 一下.

```python
def forward(self, x, t, class_labels):
    bs, ch, w, h = x.shape

    # & self.class_emb = nn.Embedding(num_classes, class_emb_size)
    class_cond = self.class_emb(class_labels) # *
    # 广播
    class_cond = class_cond.view(bs, class_cond.shape[1], 1, 1).expand(bs, class_cond.shape[1], w, h)

    net_input = torch.cat((x, class_cond), dim=1)

    # model 返回 ModelOutput.
    # sample: 就是预测的噪声张量.
    # additional_residuals: 存储额外残差信息. 一般没用.
    return self.model(net_input, t).sample
```

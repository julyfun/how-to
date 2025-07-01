---
title: linear
date: 2024-01-15 01:10:05
tags: ["learn", "d2l"]
---
## 典型线性回归训练过程

我不知道哪句话是给 backward() 做准备的，估计是 loss() 吧。

测了一下发现 zero_grad() 好像也是必要的。我猜想不 zero_grad() 则 loss() + backword() 不会改变权重。至少不会有效地改变权重。

```py
num_epochs = 3
for epoch in range(num_epochs):
    # 调用迭代器的一组数据
    for x, y in data_iter:
        # remind: loss = nn.MSELoss()
        l = loss(net(x), y)
        # clears the gradients of all parameters in the model, 
        # ensuring that the gradients are fresh and ready to 
        # be computed for the current iteration.
        trainer.zero_grad()
        # 反向传播
        l.backward()
        # trainer 中传入了 net 的参数的引用
        trainer.step()
    l = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l:f}')
```

Chat says:

在 PyTorch 中，trainer.zero_grad()用于清除模型参数的梯度，以确保在每个迭代中梯度是新鲜的，并且可以在当前迭代中进行计算。如果你去掉了trainer.zero_grad()，会导致梯度累积，也就是说梯度不会在每个batch之间清零，而会累积到之前的梯度上。

这可能会导致两个主要问题：

梯度爆炸或梯度消失：梯度可能会变得非常大或非常小，使得优化算法不稳定，这可能导致模型无法收敛或收敛非常缓慢。

内存占用问题：梯度不清零可能会导致内存占用增加，因为梯度会持续累积，占用更多的内存。

这里的所有数据都是用一个假定的 w 和 b 生成的。让我们看看网络得到的 w 和 b 与真实的 w b 差多少。

```py
w = net[0].weight.data
print('w的估计误差：', true_w - w.reshape(true_w.shape))
b = net[0].bias.data
print('b的估计误差：', true_b - b)
```

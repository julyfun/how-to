- 作用：对于连续的状态和离散的动作，可通过采样方式更新神经网络
    - Input: state
    - Output: value of all actions
    - 这就是学了个 $Q$，有了 $Q$ 策略就是选最大价值动作。
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108230928.webp)
## 损失设计

- 由于 Q-learning 是这样的:
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108231138.webp)
- 所以对于一个批量的采样 ${(s_i, a_i, r_i, s_i^prime)}$，可以这样设计损失函数:
    - 注意这里损失函数里有 $Q$ 本身，无法方便求损失，所以设计了训练网络和目标网络。这里 $w$ 是 MLP 权重。
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108231239.webp)

## 经验回放 experience replay

将历次采样放入缓冲区，取缓冲区的若干次数据（而不是最近一次）作为一个小批量来优化 $Q_w$

## 目标网络 + 训练网络

其实就是复制两份网络，训练网络每次批量优化时都会更新（目标网络暂不更新），其中损失函数使用目标网络计算，每隔 $C$ 步将目标网络同步到训练网络。形式化的损失函数总是 $(y_i - y^hat)$

![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241108231747.webp)

done.

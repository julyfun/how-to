## Double DQN

- 上一章的 DQN 在计算 $y^"real"$ 时，使用的是:
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241111174501.webp)
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241111174533.webp)
- 如 $w^-$ 有正向误差估计，则 $Q(s, a)$ 会被过高估计，而拿 $Q(s, a)$ 更新上一步 $Q$ 时，误差会逐渐累积。
- 如何解决？将优化目标改为下式，也就是取下一步最优动作时使用训练网络而不是目标网络. 这样可以缓解此问题.
- ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241111174812.webp)



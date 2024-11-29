- [**平均互信息**]
    - ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241129102210.webp)
        - 其中 $I(x_i; y_j) = log p(x_i|y_j) / p(x_i)$ 即 X 的信息量减去知道 Y 后 X 的信息量
    - (收到 Y) 对于 X 的信息量的贡献.
    - **对称性**: $I(X; Y) = I(Y; X)$
    - **非负性**
        - 单次通信可能使 Y 的不确定性增大，但是统计平均一定是不确定性减小
    - **凸性**
        - I(X; Y) 是 关于 $p(bold(x^->))$ 向量的一个上凸函数
## 附录

- [抄的结论] $$I(x_i y_j) = I(y_j) + I(x_i | y_j)$$
- [记忆] $$p(y|x) = p(x y) / p(x) => H(Y|X) = H(X Y) - H(X)$$

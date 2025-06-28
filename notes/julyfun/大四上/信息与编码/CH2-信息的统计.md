---
title: "CH2-信息的统计"
date: 2024-11-27 02:41:30
tags: []
---
- **[自信息]**
    - 概率小 50%，信息量 + 1
        -  $I(x_i) = -log(x_i)$
- **[条件自信息]**
    - ...
- **[互信息]
    - 用于衡量两个随机变量之间相互依赖性的量（成功传输的信息）
    - $I(X; Y) = H(X) - H(X | Y) = H(Y) - H(Y | X)$
- **[信源熵]**
    - 就是自信息的期望, 对于无记忆信源. 是一个先验概率:
    - $$H(X) = E[I(X)] = sum_(i = 1)^n p(x_i) I(x_i) = - sum_(i = 1)^n p(x_i) log p(x_i)$$
    - 单位 bit/symbol （信息每符号）。符号几率越平均，熵越大
        - 还有后验概率版本，即接收到了以后反算熵.
- **[条件熵]**
    - 即条件自信息的期望. $H(Y|X)$ 为已知随机变量 $X$ 的条件下随机变量 $Y$ 的不确定性.
    - **[噪声熵]**: X 给到 Y 以后 Y 还有多少噪声.
        - ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121103813.webp)

    - **[损失熵]**:
        - X 的多少信息没传过去.
            - 例子：$x_1 tilde x_8$ 必导致 $y_1$, $x_9 tilde x_16$ 必导致 $y_2$，
                - 则噪声熵为 $0$，损失熵 $3$，联合熵 
        - ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121103832.webp)
- **[联合熵 Joint Entropy]**:
    - ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121103923.webp)
- 不确定性图:
    - ![image.png|300](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121104058.webp)
    - ![image.png|600](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121104156.webp)
    - ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121104255.webp)
    - 例:
        -  ![image.png|300](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121105919.webp)
        - ![image.png|600](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241121105909.webp)
    - 例:
        - ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241122210240.webp)

- **[熵函数的属性]**
    - 非负性
    - 对称性: 交换概率，熵不变
    - 确定性：如果存在一个概率 = 1，则信息量为 0.
    - 扩展性: 将其中一个 $p_i$ 分出一个极小量到另一个符号，熵不变.
    - 强可加性:
        - $H(X Y) = H(X) + H(Y | X)$
        - 可加性: s-独立时有 $H(X Y) = H(X) + H(Y)$
    - 增性:
        - 将其中一个符号 $x$ 拆分成若干个符号（概率和为 $x$），熵增加.
    - 上凸性:
        - 对概率向量 $P$，$H$ 是上凸的
    - 极限性质：
        - 对于离散信源, 当各个符号概率一样的时候，$H$ 最大.
## 例题

- **[问]** $[1 / 2, 1 / 4, 1 / 8, 1/ 8]$ 信源的熵
    - $$1 dot 1 / 2 + 2 dot 1 / 4 + 3 dot 1 / 8 dot 2 = 4 / 7 "bits/symbol"$$
    - 可以用变长码（哈夫曼编码）来表示这些符号，可以做到平均编码长度为 $1.75$
    
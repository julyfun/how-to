---
title: CH3-离散和连续源的信息熵
date: 2024-11-27 02:41:30
tags: ["notes", "julyfun", "大四上", "信息与编码"]
---
- **[Chain rules for Entropy]**
    - 计算有记忆源的信息熵公式.
    - $$H(X^N) = sum_(i = 1)^N H(X_i | X_(1..i - 1))$$
- **[带记忆多符号离散平稳源的极限熵]**
    - 定义为:  ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241122170613.webp)
    - ![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241122170649.webp)
        - 平均符号熵和条件熵都会趋于稳定值（极限熵）.
            - [?]
 
## 连续熵

 - [微分熵] 
    - 这是去掉无穷大项以后的相对熵.
     - $$h(X) = - integral_S f(x) log f(x) dif x$$
    - 计算机内部先离散.
- **[正态分布熵]**
    - 逆天，我推的. 注意积 $e^(-t^2)t^2$ 时，令 $u = e^(-t^2)t, v = t$:

$$
integral e^(-t^2) t^2 dif t &= u^circle v - u^(circle circle) v^prime \
&= [-1 / 2 e^(-t^2) dot t]_(-oo)^(+oo) - integral -1 / 2 e^(-t^2) dif t \
&= 0 + 1 / 2 sqrt(pi)
$$
![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241128115147.webp)

- 最大熵定理
    - 同样方差情况下，正态分布熵最大.
- $H_0$ : 符号等概率分布情况下具有的熵. $= log_2 "符号数量"$
- 利用率 $eta = H_"real"(X) / (H_0(X))$, 冗余度 $gamma = 1 - eta$
- 信源编码：冗余度越小越好
    - 信道编码：需要增加一些冗余度以提升抗干扰性.

## 杂项

- 条件熵一定小于无条件熵

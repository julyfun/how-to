## 数学形式
$$F(omega) = integral_(-oo)^(+oo) f(t) e^(-i t x) dif t$$
$$
f(t) = cal(F)^(-1)[F(omega)] = 1 / (2pi) integral_(-oo)^(+oo) F(w) e^(i w t) dif omega
$$
ref: https://the-art-of-programming-by-july.readthedocs.io/en/latest/ebook/zh/%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2%E7%AE%97%E6%B3%95%E3%80%81%E4%B8%8A/

## FFT 求频谱相关

FFT 就是快速 DFT。你的数据采样间隔 $T_s$，采样 $N$ 次，采样周期 $T_0 = N T_s$

做 FFT 并绘制，你将得到最大频率 $1 / (2 T_s)$，基准频率（分度值）为 $1 / (N T_s)$ 的频谱：

```py
N = len(x)  # Number of samples
T = 1.0 / 200.0 # Sampling interval (1/200 Hz)
yf = np.fft.fft(x) # Compute the FFT 频率分量
xf = np.fft.fftfreq(N, T)[:N // 2] # 获取实际频率作为横轴

# Plot the frequency spectrum
plt.plot(xf, 2.0 / N * np.abs(yf[:N // 2])) # Normalize and plot
```

ref: https://zhuanlan.zhihu.com/p/620462217 含有 FFT 算法证明

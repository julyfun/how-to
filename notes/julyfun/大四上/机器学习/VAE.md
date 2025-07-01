---
title: VAE
date: 2024-12-12 14:35:11
tags: ["notes", "julyfun", "大四上", "机器学习"]
---
- 关于 VAE 理解的教程： https://spaces.ac.cn/archives/5253

- 假定 $p(Z|X)$ 为一正态分布.（Z 为隐变量，X 为目标分布）
    - 注意不是假设 $p(Z)$为正态分布，不同 $X$ 显然必须有不同的隐藏分布，否则解码器无法区分它们，训练时 $X_i$ 和 $X^"hat"_i$ 就无法对应上.
- 训练编码器使得样本对应的（编码器输出的）$mu$ 和 $log sigma^2$ 既要接近正态分布，又要对不同样本产生一些区别使得解码器能够将其还原到对应图像.
    - 接近正态又要有些微区分，这是一个权衡问题.
    - 为了防止正态分布采样以后，不同样本直接混在一起，其实不同类图像还是独占某一隐变量空间的区域的（这个我主成分分析绘制过）.
- Hint:
    - 正态分布的参数为 runtime 参数（中间层输出结果），不是 traintime 权重. 

大致代码（见 speit-ml-tp 仓库） :

```python
from torch.nn.functional import binary_cross_entropy
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

class Sampling(nn.Module):
    def forward(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

class Encoder(nn.Module):
    def __init__(self, latent_dim):
        super(Encoder, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.fc = nn.Linear(64 * 7 * 7, 16)
        self.fc_mu = nn.Linear(16, latent_dim)
        self.fc_logvar = nn.Linear(16, latent_dim)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc(x))
        mu = self.fc_mu(x)
        logvar = self.fc_logvar(x)
        return mu, logvar

class Decoder(nn.Module):
    def __init__(self, latent_dim):
        super(Decoder, self).__init__()
        self.fc = nn.Linear(latent_dim, 64 * 7 * 7)
        self.deconv1 = nn.ConvTranspose2d(64, 64, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.deconv2 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.deconv3 = nn.ConvTranspose2d(32, 1, kernel_size=3, padding=1)

    def forward(self, z):
        x = torch.relu(self.fc(z))
        x = x.view(-1, 64, 7, 7)
        x = torch.relu(self.deconv1(x))
        x = torch.relu(self.deconv2(x))
        x = torch.sigmoid(self.deconv3(x))
        return x

class VAE(nn.Module):
    def __init__(self, latent_dim):
        super(VAE, self).__init__()
        self.encoder = Encoder(latent_dim)
        self.decoder = Decoder(latent_dim)
        self.sampling = Sampling()

    def forward(self, x):
        mu, logvar = self.encoder(x)
        z = self.sampling(mu, logvar)
        return self.decoder(z), mu, logvar

def loss_function(recon_x, x, mu, logvar): # reconstruction
    BCE = binary_cross_entropy(recon_x, x, reduction='sum')
    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return BCE + KLD
```

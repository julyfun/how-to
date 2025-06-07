# %%
from collections import namedtuple
def test(func):
    func()

# %%
import torch
import torchvision
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from diffusers import DDPMScheduler, UNet2DModel
from matplotlib import pyplot as plt

device = torch.device("cuda")
print(f"Using device: {device}")
# %%

dataset = torchvision.datasets.MNIST(root="ignoreme-mnist/", train=True, download=True, transform=torchvision.transforms.ToTensor())

# %%

train_loader = DataLoader(dataset, batch_size=8, shuffle=True)

# %%

from torchvision.utils import make_grid 
x, y = next(iter(train_loader))
print(f"x.shape: {x.shape}, y.shape: {y.shape}")    
plt.imshow(make_grid(x)[0], cmap="Greys")
print(make_grid(x).shape)

# %%
def corrupt(x, amount): # amount of shape (B,)
    noise = torch.rand_like(x)
    amount = amount.view(-1, 1, 1, 1)
    return noise * amount + x * (1 - amount), noise

# %%
amount = torch.linspace(0, 1, x.shape[0])
print(amount.shape, amount) # torch.size([8])
noised_x, noise = corrupt(x, amount)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(make_grid(x)[0], cmap="Greys")
axs[1].imshow(make_grid(noised_x)[0], cmap="Greys")

@test
def main():
    x = torch.randn(8, 1, 28, 28)
    assert corrupt(x, amount)[0].shape == x.shape, "Corrupted shape should match original shape"
# %%

class BasicUNet(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()

        self.downs_layers = nn.ModuleList([
            nn.Conv2d(in_channels, 32, kernel_size=5, padding=2),
            nn.Conv2d(32, 64, kernel_size=5, padding=2),
            nn.Conv2d(64, 64, kernel_size=5, padding=2),
        ])
        self.up_layers = nn.ModuleList([    
            nn.Conv2d(64, 64, kernel_size=5, padding=2),
            nn.Conv2d(64, 32, kernel_size=5, padding=2),
            nn.Conv2d(32, out_channels, kernel_size=5, padding=2),
        ])
        self.act = nn.SiLU()
        self.downscale = nn.MaxPool2d(kernel_size=2)
        self.upscale = nn.Upsample(scale_factor=2) # 暴力上采样

    def forward(self, x):
        h = []
        for i, l in enumerate(self.downs_layers):
            x = self.act(l(x))
            if i < 2: # 除最后一层以外，有 residual connection（这里是直接加不是拼接）
                h.append(x)
                x = self.downscale(x)

        for i, l in enumerate(self.up_layers):
            if i > 0:
                x = self.upscale(x)
                x += h.pop()
            x = self.act(l(x))

        return x

# %%

net = BasicUNet(in_channels=1, out_channels=1)
x = torch.randn(8, 1, 28, 28)
print(net(x).shape)

print(sum([p.numel() for p in net.parameters() if p.requires_grad]) )
sum([p.numel() for p in net.parameters()]) 


# %%
bs = 128
train_loader = DataLoader(dataset, batch_size=bs, shuffle=True)
n_epochs = 3
net = BasicUNet(in_channels=1, out_channels=1).to(device)

loss_fn = nn.MSELoss()
opt = torch.optim.Adam(net.parameters(), lr=1e-3)
losses = []

for epoch in range(n_epochs):
    for x, y in train_loader:
        x = x.to(device)
        noise_amount = torch.rand(x.shape[0]).to(device)
        noisy_x, noise = corrupt(x, noise_amount)

        pred_noise = net(noisy_x)
        loss: torch.Tensor = loss_fn(pred_noise, noise)

        opt.zero_grad()
        loss.backward()
        opt.step()

        losses.append(loss.item())
        

plt.plot(losses)
plt.ylim(0, 0.1)

# %%
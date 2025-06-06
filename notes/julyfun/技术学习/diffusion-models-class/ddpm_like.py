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
    return noise * amount + x * (1 - amount)

# %%
amount = torch.linspace(0, 1, x.shape[0])
print(amount.shape, amount) # torch.size([8])
noised_x = corrupt(x, amount)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(make_grid(x)[0], cmap="Greys")
axs[1].imshow(make_grid(noised_x)[0], cmap="Greys")

# %%
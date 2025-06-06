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
type(make_grid(x).shape)

# %%
# %%
import torch
import torchvision
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from diffusers import DDPMScheduler, UNet2DModel
from matplotlib import pyplot as plt
from tqdm.auto import tqdm

device = 'cuda'
print(f'Using device: {device}')

mg = torchvision.utils.make_grid

# %%

dataset = torchvision.datasets.MNIST(root="ignoreme-mnist/", train=True, download=False, transform=torchvision.transforms.ToTensor())

train_dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

x, y = next(iter(train_dataloader))

print('Input shape:', x.shape, 'Output shape:', y.shape)

print(mg(x).shape)
plt.imshow(mg(x)[0], cmap='Greys')


# %%
class ClassConditionedUnet(nn.Module):
    def __init__(self, num_classes, class_emb_size=4):
        super().__init__()

        self.class_emb
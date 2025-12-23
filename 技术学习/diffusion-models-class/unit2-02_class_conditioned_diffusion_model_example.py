# %%
import torch
import torchvision
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from diffusers import DDPMScheduler, UNet2DModel
from matplotlib import pyplot as plt
from tqdm.auto import tqdm
# python executable path
from robotoy.ziglike.test import test, enable_testing, run

device = 'cuda'
print(f'Using device: {device}')

mg = torchvision.utils.make_grid

# %%
dataset = torchvision.datasets.MNIST(root="ignoreme-mnist/", train=True, download=False, transform=torchvision.transforms.ToTensor())
train_dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

# 数据集的 label 作为网络输入一部分
x, y = next(iter(train_dataloader))

print('Input shape:', x.shape, 'Output shape:', y.shape)

print(mg(x).shape)
plt.imshow(mg(x)[0], cmap='Greys')

# %%
class ClassConditionedUnet(nn.Module):
    def __init__(self, num_classes, class_emb_size=4):
        super().__init__()
        # nn.Embedding(输入范围, 输出维度)
        self.class_emb = nn.Embedding(num_classes, class_emb_size)
        self.model = UNet2DModel(
            sample_size=28, # the target image resolution
            in_channels=1 + class_emb_size,
            out_channels=1,
            layers_per_block=2,
            block_out_channels=(32, 64, 64),
            down_block_types=(
                "DownBlock2D",
                "AttnDownBlock2D", # spatial self-attention
                "AttnDownBlock2D",
            ),
            up_block_types=(
                "AttnUpBlock2D",
                "AttnUpBlock2D",
                "UpBlock2D",
            ),
        )

    def forward(self, x, t, class_labels):
        bs, ch, w, h = x.shape

        class_cond = self.class_emb(class_labels)
        class_cond = class_cond.view(bs, class_cond.shape[1], 1, 1).expand(bs, class_cond.shape[1], w, h)

        net_input = torch.cat((x, class_cond), dim=1)

        # model 返回 ModelOutput.
        # sample: 就是预测的噪声张量.
        # additional_residuals: 存储额外残差信息. 一般没用.
        return self.model(net_input, t).sample

# %%
init_mem = torch.cuda.memory_allocated(device)
@run
def func():
    net = ClassConditionedUnet(num_classes=10).to(device)
    img = torch.randn(3, 1, 28, 28).to(device)
    cls = torch.tensor([0, 1, 9]).to(device)
    t = torch.randn(3).to(device)
    print(net(img, t, cls).shape)
    fin_mem = torch.cuda.memory_allocated(device)
    print(f"{fin_mem - init_mem} bytes")

# %%
net = ClassConditionedUnet(num_classes=10).to(device)
noise_scheduler = DDPMScheduler(num_train_timesteps=1000, beta_schedule="squaredcos_cap_v2")
losses = []
loss_fn = nn.MSELoss()
opt = torch.optim.Adam(net.parameters(), lr=1e-3)

train_dataloader = DataLoader(dataset, batch_size=128, shuffle=True)

for epoch in range(n_epochs := 10):
    for x, y in tqdm(train_dataloader):
        x = x.to(device) * 2 - 1
        y = y.to(device)
        noise = torch.randn_like(x)
        timesteps = torch.randint(0, 999, size=(x.shape[0],)).long().to(device)
        noisy_x = noise_scheduler.add_noise(x, noise, timesteps)

        pred = net(noisy_x, timesteps, y) # Here labels are passed in!
        loss = loss_fn(pred, noise)

        opt.zero_grad()
        loss.backward()
        opt.step()

        losses.append(loss.item())

plt.plot(losses)
# %%
# show parameter nums
print(sum(p.numel() for p in net.parameters()))

# %%
# x 纯噪声
x = torch.randn(80, 1, 28, 28).to(device)
# y 是 class
y = torch.tensor([[i] * 8 for i in range(10)]).flatten().to(device)
noise_scheduler.timesteps

# %%
for i, t in tqdm(enumerate(noise_scheduler.timesteps)):
    with torch.no_grad():
        residual = net(x, t, y) # 输出的具体是啥取决于是 eps-参数化还是 x_0 参数化

    x = noise_scheduler.step(residual, int(t), x).prev_sample

fig, ax = plt.subplots(1, 1, figsize=(12, 12))
ax.imshow(mg(x.detach().cpu().clip(-1, 1), nrow=8)[0], cmap='Greys')

# %%
if __name__ == "__main__":
    enable_testing()

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
def flow_interpolate(x, t): # t of shape (B,) in [0, 1]
    """Linear interpolation path: x_t = t * x + (1-t) * noise"""
    noise = torch.randn_like(x)
    t = t.view(-1, 1, 1, 1)
    x_t = t * x + (1 - t) * noise
    # Velocity field: dx/dt = x - noise (constant velocity)
    velocity = x - noise
    return x_t, velocity

# %%
t = torch.linspace(0, 1, x.shape[0])
print(t.shape, t) # torch.size([8])
x_t, velocity = flow_interpolate(x, t)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].set_title("Original")
axs[0].imshow(make_grid(x)[0], cmap="Greys")
axs[1].set_title("Interpolated")
axs[1].imshow(make_grid(x_t)[0], cmap="Greys")
axs[2].set_title("Velocity Field")
axs[2].imshow(make_grid(velocity)[0], cmap="Greys")

@test
def main():
    x = torch.randn(8, 1, 28, 28)
    t = torch.rand(8)
    x_t, v = flow_interpolate(x, t)
    assert x_t.shape == x.shape, "Interpolated shape should match original shape"
    assert v.shape == x.shape, "Velocity shape should match original shape"

# %%
class FlowUNet(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()

        # Time embedding
        self.time_embed = nn.Sequential(
            nn.Linear(1, 32),
            nn.SiLU(),
            nn.Linear(32, 32)
        )

        self.downs_layers = nn.ModuleList([
            nn.Conv2d(in_channels + 32, 32, kernel_size=5, padding=2),  # +32 for time embedding
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
        self.upscale = nn.Upsample(scale_factor=2)

    def forward(self, x, t):
        # Time embedding
        t_embed = self.time_embed(t.view(-1, 1))  # (B, 32)
        t_embed = t_embed.view(-1, 32, 1, 1).expand(-1, -1, x.shape[2], x.shape[3])  # (B, 32, H, W)

        # Concatenate input with time embedding
        x = torch.cat([x, t_embed], dim=1)

        h = []
        for i, l in enumerate(self.downs_layers):
            x = self.act(l(x))
            if i < 2:
                h.append(x)
                x = self.downscale(x)

        for i, l in enumerate(self.up_layers):
            if i > 0:
                x = self.upscale(x)
                x += h.pop()
            x = self.act(l(x))

        return x

# %%
net = FlowUNet(in_channels=1, out_channels=1)
x = torch.randn(8, 1, 28, 28)
t = torch.rand(8)
print(net(x, t).shape)

print("Parameters:", sum([p.numel() for p in net.parameters() if p.requires_grad]))

# %%
bs = 128
train_loader = DataLoader(dataset, batch_size=bs, shuffle=True)
n_epochs = 3
net = FlowUNet(in_channels=1, out_channels=1).to(device)

loss_fn = nn.MSELoss()
opt = torch.optim.Adam(net.parameters(), lr=1e-3)
losses = []

for epoch in range(n_epochs):
    for x, y in train_loader:
        x = x.to(device)
        # Sample random time steps
        t = torch.rand(x.shape[0]).to(device)

        # Get interpolated data and true velocity
        x_t, true_velocity = flow_interpolate(x, t)
        x_t = x_t.to(device)
        true_velocity = true_velocity.to(device)

        # Predict velocity field
        pred_velocity = net(x_t, t)
        loss: torch.Tensor = loss_fn(pred_velocity, true_velocity)

        opt.zero_grad()
        loss.backward()
        opt.step()

        losses.append(loss.item())

    print(f"Epoch {epoch + 1}, Loss: {losses[-1]:.4f}")

plt.plot(losses)
plt.title("Flow Matching Training Loss")
plt.xlabel("Steps")
plt.ylabel("MSE Loss")

# %%
# Visualization of learned velocity field
x, y = next(iter(train_loader))
x = x[:8]

t = torch.linspace(0, 0.9, x.shape[0])
x_t, true_velocity = flow_interpolate(x, t)

with torch.no_grad():
    pred_velocity = net(x_t.to(device), t.to(device)).detach().cpu()

fig, axs = plt.subplots(4, 1, figsize=(12, 10))
axs[0].set_title("Original")
axs[0].imshow(make_grid(x)[0].clip(0, 1), cmap="Greys")

axs[1].set_title("Interpolated x_t")
axs[1].imshow(make_grid(x_t)[0].clip(0, 1), cmap="Greys")

axs[2].set_title("True Velocity")
axs[2].imshow(make_grid(true_velocity)[0], cmap="RdBu_r", vmin=-1, vmax=1)

axs[3].set_title("Predicted Velocity")
axs[3].imshow(make_grid(pred_velocity)[0], cmap="RdBu_r", vmin=-1, vmax=1)

# %%
# Flow sampling using Euler integration
def euler_sample(net, shape, n_steps=20, device=device):
    """Sample using Euler integration of the learned flow"""
    with torch.no_grad():
        # Start from noise
        x = torch.randn(shape).to(device)
        dt = 1.0 / n_steps

        trajectory = [x.detach().cpu()]

        for step in range(n_steps):
            t = torch.full((shape[0],), step * dt).to(device)

            # Predict velocity and integrate
            velocity = net(x, t)
            x = x + velocity * dt

            trajectory.append(x.detach().cpu())

    return trajectory

# %%
# Generate samples
n_samples = 8
trajectory = euler_sample(net, (n_samples, 1, 28, 28), n_steps=20)

# Visualize sampling trajectory
n_display_steps = 5
step_indices = [0, 5, 10, 15, 19]  # Show steps at different stages

fig, axs = plt.subplots(len(step_indices), 1, figsize=(12, 10))
for i, step_idx in enumerate(step_indices):
    axs[i].set_title(f"Step {step_idx}/20 (t={step_idx/20:.2f})")
    axs[i].imshow(make_grid(trajectory[step_idx])[0].clip(0, 1), cmap="Greys")

plt.tight_layout()

# %%
# Compare final samples with real data
real_x, _ = next(iter(train_loader))
real_x = real_x[:8]

final_samples = trajectory[-1]

fig, axs = plt.subplots(2, 1, figsize=(12, 6))
axs[0].set_title("Real Data")
axs[0].imshow(make_grid(real_x)[0].clip(0, 1), cmap="Greys")

axs[1].set_title("Generated Samples")
axs[1].imshow(make_grid(final_samples)[0].clip(0, 1), cmap="Greys")

plt.tight_layout()

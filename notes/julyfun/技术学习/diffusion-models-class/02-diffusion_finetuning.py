# %%

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

device = 'cuda'

# %%
from diffusers import DDIMScheduler, DDPMPipeline

image_pipe = DDPMPipeline.from_pretrained('google/ddpm-celebahq-256')

# %%

image_pipe.to(device)

# %%

DDPMPipeline.__mro__
# %%

# Generate images using ()
imgs = image_pipe().images
imgs[0]

# %%

# [Train a new scheduler] Later replace the scheduler in the image_pipe
scheduler = DDIMScheduler.from_pretrained('google/ddpm-celebahq-256')

scheduler.set_timesteps(num_inference_steps=40)
# %%

scheduler.timesteps # 输出 like [975, 950, ...]

# %%
from tqdm import tqdm
import torchvision
from matplotlib import pyplot as plt
make_grid = torchvision.utils.make_grid

x = torch.randn((4, 3, 256, 256), device=device)

for i, t in tqdm(enumerate(scheduler.timesteps)):
    # prepare
    input = scheduler.scale_model_input(x, t)
    with torch.no_grad():
        noise_pred = image_pipe.unet(input, t)["sample"]

    # predict all data
    scheduler_output = scheduler.step(noise_pred, t, sample=x)
    x = scheduler_output.prev_sample

    if i % 10 == 0 or i == len(scheduler.timesteps) - 1:
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        grid = make_grid(x, nrow=4).permute(1, 2, 0)

        axs[0].imshow(grid.cpu().clip(-1, 1) * 0.5 + 0.5)
        axs[0].set_title(f"Current x (step {i})")

        # 预测的完全去噪结果
        pred_x0 = scheduler_output.pred_original_sample
        grid = make_grid(pred_x0, nrow=4).permute(1, 2, 0)
        axs[1].imshow(grid.cpu().clip(-1, 1) * 0.5 + 0.5)
        axs[1].set_title(f"Predicted denoised (step {i})")
        plt.show()

# %%

image_pipe.scheduler = scheduler
images = image_pipe(num_inference_steps=40).images
images[0]

# %%

from datasets import load_dataset
from torchvision import transforms

dataset_name = "huggan/smithsonian_butterflies_subset"
dataset = load_dataset(dataset_name, split="train")

image_size = 256
batch_size = 4

preprocess = transforms.Compose(
    [
        transforms.Resize((image_size, image_size)),
        transforms.RandomHorizontalFlip(), # 50% 概率水平翻转
        transforms.ToTensor(),
        transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]), # (x - mean) / std
    ]
)


# %%

# PIL -> preprocess -> tensor
def transform(examples):
    images = [preprocess(image.convert("RGB")) for image in examples["image"]]
    return {"images": images}

dataset.set_transform(transform)

train_dataloader = torch.utils.data.DataLoader(
    dataset, batch_size=batch_size, shuffle=True
)

batch = next(iter(train_dataloader))
grid = torchvision.utils.make_grid(batch["images"], nrow=4)
plt.imshow(grid.permute(1, 2, 0).cpu().clip(-1, 1) * 0.5 + 0.5) # imshow 要求 [H, W, C]

# %%

num_epochs = 2

for epoch in range(num_epochs):
    for step, batch in enumerate(tqdm(train_dataloader)):

        clean_images = batch["images"].to(device)
        noise = torch.randn_like(clean_images).to(device)

        bs = clean_images.shape[0] # batch size

        timesteps: torch.Tensor = torch.randint(
            0,
            image_pipe.scheduler.num_inference_steps
        )

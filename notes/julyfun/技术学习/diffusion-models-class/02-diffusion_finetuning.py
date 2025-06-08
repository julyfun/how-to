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

        pred_x0 = scheduler_output.pred_original_sample
        grid = make_grid(pred_x0, nrow=4).permute(1, 2, 0)
        axs[1].imshow(grid.cpu().clip(-1, 1) * 0.5 + 0.5)
        axs[1].set_title(f"Predicted denoised (step {i})")

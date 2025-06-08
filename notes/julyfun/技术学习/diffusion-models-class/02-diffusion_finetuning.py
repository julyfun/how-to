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

x = torch.randn((4, 3, 256, 256), device=device)

for i, t in tqdm(enumerate(scheduler.timesteps)):
    input = scheduler.scale_model_input(x, t)
    with torch.no_grad():
        noise_pred = image_pipe.unet(input, t)["sample"]
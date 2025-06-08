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
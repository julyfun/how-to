# %%
import torch
import requests
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plt

from diffusers import (
    StableDiffusionPipeline,
    StableDiffusionImg2ImgPipeline,
)

def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

img_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"
mask_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"

img_height = 512
img_width = 512

init_image = download_image(img_url).resize((img_height, img_width))
mask_img = download_image(mask_url).resize((img_height, img_width))

device = 'cuda'

# %%

model_id = "stabilityai/stable-diffusion-2-1-base"
pipe = StableDiffusionPipeline.from_pretrained(model_id).to(device)

# %%
def numel(model):
    return sum(p.numel() for p in model.parameters())

numel(pipe.vae), numel(pipe.unet), numel(pipe.text_encoder)
# %%
type(pipe.tokenizer)

# %%
from torchinfo import summary

summary(
    pipe.vae,
    input_size=(1, 4, 64, 64),
    col_names = ["output_size", "num_params"],
    verbose=0
)
# %%
txt = ["a lotta cute dogs", "Trump and trump"]
tokens = pipe.tokenizer(txt, padding=True, truncation=True, return_tensors="pt")
tokens

# %%
def print_inheritance_tree(cls, indent='', last=True, is_root=True):
    if is_root:
        print(cls.__name__)
    else:
        connector = '└── ' if last else '├── '
        print(indent + connector + cls.__name__)
        indent += '    ' if last else '│   '
    bases = cls.__bases__
    for i, base in enumerate(bases):
        is_last = i == (len(bases) - 1)
        print_inheritance_tree(base, indent, is_last, is_root=False)

# Example classes
class A: pass
class B(A): pass
class C(B): pass
class D(A): pass
class E(D, C): pass

print_inheritance_tree(type(pipe.text_encoder))
# %%
print(list(pipe.components.keys()))

# %%

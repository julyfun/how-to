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
    input_size=(1, 3, 64, 64),
    col_names = ["output_size", "num_params"],
    verbose=0,
    depth=3,
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

gen  = torch.Generator(device=device).manual_seed(42)
pipe_out = pipe(
    prompt="British shorthair in the house, cute, high quality",
    negative_prompt="Oversaturated, blurry, low quality",
    height=480, width=480,
    guidance_scale=2,
    num_inference_steps=35,
    generator=gen
)

pipe_out.images[0]

# %%
# [copy]
cfg_scales = [1.1, 8, 12] #@param
prompt = "A collie with a pink hat" #@param
fig, axs = plt.subplots(1, len(cfg_scales), figsize=(16, 5))
for i, ax in enumerate(axs):
  im = pipe(prompt, height=480, width=480,
    guidance_scale=cfg_scales[i], num_inference_steps=35,
    generator=torch.Generator(device=device).manual_seed(42)).images[0]
  ax.imshow(im); ax.set_title(f'CFG Scale {cfg_scales[i]}');
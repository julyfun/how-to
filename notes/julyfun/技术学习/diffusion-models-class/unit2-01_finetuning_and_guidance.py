# %%
# [utils]
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from diffusers import DDIMScheduler, DDPMPipeline
from tqdm import tqdm
import torchvision
from PIL import Image
from matplotlib import pyplot as plt
device = 'cuda'
make_grid = torchvision.utils.make_grid

# %%

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
        # (x - mean) / std，其实就是 * 2 - 1
        transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
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
losses=  []
grad_accumulation_steps = 2

# 只优化 unet
opt = torch.optim.AdamW(image_pipe.unet.parameters(), lr=1e-5)

for epoch in range(num_epochs):
    for step, batch in enumerate(tqdm(train_dataloader)):

        clean_images = batch["images"].to(device)
        noise = torch.randn_like(clean_images).to(device)

        bs = clean_images.shape[0] # batch size

        timesteps: torch.Tensor = torch.randint(
            0,
            image_pipe.scheduler.num_inference_steps,
            (bs,),
            device=device,
        ).long()

        noisy_images = image_pipe.scheduler.add_noise(
            clean_images,
            noise,
            timesteps
        )

        noise_pred = image_pipe.unet(noisy_images, timesteps, return_dict=False)
        noise_pred = noise_pred[0]

        loss = F.mse_loss(noise_pred, noise)
        losses.append(loss.item())
        loss.backward(loss)

        # [梯度累积] 变相增大 batch size，而无需更大 GPU MEM。lr 需要减小。
        if (step + 1) % grad_accumulation_steps == 0:
            opt.step()
            opt.zero_grad()

    print(
        f"Epoch {epoch} ave loss: {sum(losses[len(train_dataloader):]) / len(train_dataloader)}"
    )


plt.plot(losses)

# %%

len(train_dataloader) # is 250

# %%
images = image_pipe(num_inference_steps=40).images  
images[0]

# %%
image_pipe.save_pretrained("ignoreme-finetuned_butterflies-bad")

# %%
!ls {"ignoreme-finetuned_butterflies-bad"}

# %%
from huggingface_hub import HfApi, ModelCard, create_repo, get_full_repo_name

model_name = "ddpm-celebahq-finetuned-bufferflies-2epochs"
local_folder_name = "ignoreme-finetuned_butterflies-bad"
desc = "Something for test "

hub_model_id = get_full_repo_name(model_name)
create_repo(hub_model_id)

api = HfApi()
api.upload_folder(
    folder_path=f"{local_folder_name}/scheduler", path_in_repo="",
    repo_id=hub_model_id
)

api.upload_folder(
    folder_path=f"{local_folder_name}/unet", path_in_repo="",
    repo_id=hub_model_id
)

# %%

api.upload_file(
    path_or_fileobj=f"{local_folder_name}/model_index.json", path_in_repo="model_index.json",
    repo_id=hub_model_id
)

content = f"""

## Usage
---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

{desc}

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('{hub_model_id}')
image = pipeline().images[0]
image
```
"""

card = ModelCard(content)
card.push_to_hub(hub_model_id)

# %%
name = "johnowhitaker/sd-class-wikiart-from-bedrooms"
image_pipe = DDPMPipeline.from_pretrained(name).to(device)

scheduler = DDIMScheduler.from_pretrained(name)

scheduler.set_timesteps(num_inference_steps=40) 

x = torch.randn(8, 3, 256, 256).to(device)

# %%

for i, t in tqdm(enumerate(scheduler.timesteps)):
    model_input = scheduler.scale_model_input(x, t)
    with torch.no_grad():
        noise_pred = image_pipe.unet(model_input, t)["sample"]
    x = scheduler.step(noise_pred, t, sample=x).prev_sample

# %%

grid = make_grid(x, nrow=4)
plt.imshow(grid.permute(1, 2, 0).cpu().clip(-1, 1) * 0.5 + 0.5)


# %%
type(image_pipe.scheduler)

# %%

def color_loss(images, target_color=(0.1, 0.9, 0.5)):
    target = (
        torch.tensor(target_color, device=images.device) * 2 - 1
    )
    target = target[
        None, :, None, None
    ] # None 位置会插入维度为 1
    error = torch.abs(images - target).mean() # 得到一个数
    return error

# %%

import open_clip

clip_model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-32", pretrained="openai"
)

clip_model.to(device)

# %%

tfms = torchvision.transforms.Compose(
    [
        torchvision.transforms.RandomResizedCrop(224),  # Random CROP each time
        torchvision.transforms.RandomAffine(
            5
        ),  # One possible random augmentation: skews the image
        torchvision.transforms.RandomHorizontalFlip(),  # You can add additional augmentations if you like
        torchvision.transforms.Normalize(
            mean=(0.48145466, 0.4578275, 0.40821073),
            std=(0.26862954, 0.26130258, 0.27577711),
        ),
    ]
)

# %%

def clip_loss(image, text_features):
    image_features = clip_model.encode_image(tfms(image)) # of shape (bs, features_dim)
    input_normed = torch.nn.functional.normalize(image_features.unsqueeze(1), dim=2)
    embed_normed = torch.nn.functional.normalize(text_features.unsqueeze(0), dim=2)
    dists = (
        input_normed.sub(embed_normed).norm(dim=2).div(2).arcsin().pow(2).mul(2)
    )
    return dists.mean()


# %%

prompt = "Fog, forests, blue sky"

guidance_scale = 8
n_cuts = 8

scheduler.set_timesteps(50)

text = open_clip.tokenize([prompt]).to(device)

with torch.no_grad():
    text_features = clip_model.encode_text(text)
    print(f"text_features.shape: {text_features.shape}") # [1, 512]

x = torch.randn(4, 3, 256, 256).to(device)

# %%

for i, t in tqdm(enumerate(scheduler.timesteps)):
    # print(i, t) # (1, tensor(1000)), (2, tensor(980))...
    model_input = scheduler.scale_model_input(x, t) # DDIM loaded
    with torch.no_grad():
        # image_pipe is loaded by the same name
        noise_pred = image_pipe.unet(model_input, t)["sample"]

    cond_grad = 0
    for cut in range(n_cuts):
        x = x.detach().requires_grad_()

        x0  = scheduler.step(noise_pred,t, sample=x).pred_original_sample

        loss = clip_loss(x0, text_features) * guidance_scale

        cond_grad -= torch.autograd.grad(loss, x)[0] / n_cuts

    if i % 25 == 0:
        print(f"Steps {i} loss: {loss.item()}")

    alpha_bar = scheduler.alphas_cumprod[i]
    x = x.detach() + cond_grad * alpha_bar.sqrt() # Diffusion coefficient
    x = scheduler.step(noise_pred, t, x).prev_sample

# %%
grid = make_grid(x.detach(), nrow=4)
im = grid.permute(1, 2, 0).cpu().clip(-1, 1) * 0.5 + 0.5
Image.fromarray(np.array(im * 255).astype(np.uint8))

# %%

import gradio as gr
from PIL import Image, ImageColor


# The function that does the hard work
def generate(color, guidance_loss_scale):
    target_color = ImageColor.getcolor(color, "RGB")  # Target color as RGB
    target_color = [a / 255 for a in target_color]  # Rescale from (0, 255) to (0, 1)
    x = torch.randn(1, 3, 256, 256).to(device)
    for i, t in tqdm(enumerate(scheduler.timesteps)):
        model_input = scheduler.scale_model_input(x, t)
        with torch.no_grad():
            noise_pred = image_pipe.unet(model_input, t)["sample"]
        x = x.detach().requires_grad_()
        x0 = scheduler.step(noise_pred, t, x).pred_original_sample
        loss = color_loss(x0, target_color) * guidance_loss_scale
        cond_grad = -torch.autograd.grad(loss, x)[0]
        x = x.detach() + cond_grad
        x = scheduler.step(noise_pred, t, x).prev_sample
    grid = torchvision.utils.make_grid(x, nrow=4)
    im = grid.permute(1, 2, 0).cpu().numpy().clip(-1, 1) * 0.5 + 0.5
    im = Image.fromarray(np.array(im * 255).astype(np.uint8))
    im.save("ignoreme-test.jpeg")
    return im


# See the gradio docs for the types of inputs and outputs available
inputs = [
    gr.ColorPicker(label="color", value="#55FFAA"),  # Add any inputs you need here
    gr.Slider(label="guidance_scale", minimum=0, maximum=30, value=3),
]
outputs = gr.Image(label="result")

# And the minimal interface
demo = gr.Interface(
    fn=generate,
    inputs=inputs,
    outputs=outputs,
    examples=[
        ["#BB2266", 3],
        ["#44CCAA", 5],  # You can provide some example inputs to get people started
    ],
)
demo.launch(debug=True)  # debug=True allows you to see errors and output in Colab

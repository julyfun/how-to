---
title: unit2-01_finetuning_and_guidance
date: 2025-06-10 01:45:31
tags: ["notes", "julyfun", "技术学习", "diffusion-models-class"]
---
Generating process:

```python
x = torch.randn(4, 3, 256, 256).to(device)
for i, t in tqdm(enumerate(scheduler.timesteps)):
    model_input = scheduler.scale_model_input(x, t)
    with torch.no_grad():
        noise_pred = image_pipe.unet(model_input, t)["sample"]
    x = scheduler.step(noise_pred, t, sample=x).prev_sample
```

## Guidance

```python
x = torch.randn(4, 3, 256, 256).to(device)
for i, t in tqdm(enumerate(scheduler.timesteps)):
    x = x.detach().requires_grad_()
    model_input = scheduler.scale_model_input(x, t)
    noise_pred = image_pipe.unet(model_input, t)["sample"]

    x0 = scheduler.step(noise_pred, t, x).pred_original_sample
    loss = <custom_loss>(x0) * <guidance_loss_scale>
    cond_grad = -torch.autograd.grad(loss, x)[0]
    x = x.detach() + cond_grad

    x = scheduler.step(noise_pred, t, x).prev_sample
```

## CLIP Guidance

```python

with torch.no_grad():
    text_features = clip_model.encode_text(text)

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
        loss = <clip_loss>(x0, text_features) * guidance_scale
        cond_grad -= torch.autograd.grad(loss, x)[0] / n_cuts

    if i % 25 == 0:
        print(f"Steps {i} loss: {loss.item()}")

    alpha_bar = scheduler.alphas_cumprod[i]
    # `alpha_bar` here is decreasing and works for textures.
    # Can be changed to some increasing coefficients!
    x = x.detach() + cond_grad * alpha_bar.sqrt() 
    x = scheduler.step(noise_pred, t, x).prev_sample
```

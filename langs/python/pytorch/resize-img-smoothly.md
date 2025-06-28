---
title: Sample image tensor dimensions: (channels=3, height=100, width=100)
date: 2024-01-15 01:10:05
tags: []
---
## ChatGPT

```py
import cv2
import numpy as np
import torch

# Sample image tensor dimensions: (channels=3, height=100, width=100)
image_tensor = torch.rand(3, 100, 100)  # Replace with your actual tensor

# Convert PyTorch tensor to NumPy array
image_np = image_tensor.permute(1, 2, 0).cpu().numpy()  # Channels last for OpenCV

# Define the target size
target_height = 64
target_width = 64

# Resize the image using OpenCV
resized_image_np = cv2.resize(image_np, (target_width, target_height))

# Convert NumPy array back to PyTorch tensor
resized_image_tensor = torch.from_numpy(resized_image_np).permute(2, 0, 1).float()

# Print the shapes to verify
print("Original tensor shape:", image_tensor.shape)
print("Resized tensor shape:", resized_image_tensor.shape)
```

```py
import torch
import torch.nn.functional as F

# 假设你有一个480x480的RGB图片，可以表示为一个3维的torch.Tensor
# 假设img是你的原始图像，大小为(1, 3, 480, 480)
# (1, 3, 480, 480)表示(batch_size, channels, height, width)

# 生成一个480x480的假图片，这里用随机数代替
img = torch.rand(1, 3, 480, 480)

# 缩放成128x128的图像
scaled_img = F.interpolate(img, size=(128, 128), mode='bilinear', align_corners=False)

# 输出缩放后图像的大小
print("缩放后图像大小:", scaled_img.size())  # 输出: torch.Size([1, 3, 128, 128])
```

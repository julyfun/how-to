---
title: np.array is also ok!
date: 2024-01-15 01:10:05
tags: []
---
https://stackoverflow.com/questions/35286540/how-to-display-an-image

```py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('your_image.png')
# np.array is also ok!
imgplot = plt.imshow(img)
plt.show()
```


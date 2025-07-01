---
title: save-img-in-plt
date: 2024-01-15 01:10:05
tags: ["langs", "python", "matplotlib"]
---
https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it

```
    img_plot = plt.imshow(color) # color is np.array
    plt.savefig('foo.png')
    plt.show()
```


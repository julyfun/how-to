---
title: "typeerror-numpy dtypemeta-object-is-not-subscriptable-when-import-cv2"
date: 2024-01-15 01:10:05
tags: []
---

```
TypeError: 'numpy._DTypeMeta' object is not subscriptable
```

Your opencv version is too new.

Install `pip install opencv-python=4.5.1.38` solve this on numpy==1.21.5.


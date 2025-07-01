---
title: libGL-error-MESA-LOADER-failed-to-open-iris-usr-lib-dri-iris_dri-so
date: 2024-01-22 18:15:50
tags: ["langs", "python"]
---
```
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: swrast
2024-01-22 18:06:31.038 (  26.810s) [    7F77B303A740]vtkXOpenGLRenderWindow.:651    ERR| vtkXOpenGLRenderWindow (0x77ecfd0): Cannot create GLX context.  Aborting.
```

https://stackoverflow.com/questions/72110384/libgl-error-mesa-loader-failed-to-open-iris

- On Ubuntu 22.04, 24-1-22, python 3.11, using conda, taichi:

`conda install -c conda-forge libstdcxx-ng` this fixes the error


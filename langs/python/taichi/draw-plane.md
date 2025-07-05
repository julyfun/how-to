---
title: draw-plane
date: 2024-01-26 02:52:47
tags: ["langs", "python", "taichi"]
---
You need `scene.mesh()`


```py
        height = 30 / 128
        size = 1
        self.plane = vecs(3, ti.f32, 4)
        self.plane_triangles = vecs(1, ti.i32, 6)
        self.plane.from_numpy(np.array(
            [
                [0, height, 0],
                [size, height, 0],
                [size, height, size],
                [0, height, size]
            ]
        ))
        self.plane_triangles.from_numpy(np.array(
            [
                [0],
                [1],
                [2], # first triangle
                [0],
                [3],
                [2], # second
            ]
        ))

        self.scene.mesh(self.plane, self.plane_triangles)
```


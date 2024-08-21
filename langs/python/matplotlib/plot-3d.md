- reliability: "80% (author)"
- date: 2024-08-21
- language: "zh-hans"
- os: "Darwin floriandeAir 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
- author: "Julyfun MacOS14.5 M1"
- assume-you-know: [computer]

# Plot 3D

```py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

def d3(tuples):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # 解包三元组列表到X, Y, Z坐标
    X, Y, Z = zip(*tuples)
    
    # 绘制点
    ax.scatter(X, Y, Z, color='b')
    
    # 绘制线，连接相邻的点
    ax.plot(X, Y, Z, color='r')
    
    # 设置图表标题和坐标轴标签
    ax.set_title('3D Line Plot')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    ax.set_aspect('auto')
    max_range = max(max(X) - min(X), max(Y) - min(Y), max(Z) - min(Z))
    mid_x = (max(X) + min(X)) * 0.5
    mid_y = (max(Y) + min(Y)) * 0.5
    mid_z = (max(Z) + min(Z)) * 0.5
    ax.set_xlim(mid_x - max_range * 0.5, mid_x + max_range * 0.5)
    ax.set_ylim(mid_y - max_range * 0.5, mid_y + max_range * 0.5)
    ax.set_zlim(mid_z - max_range * 0.5, mid_z + max_range * 0.5)
    
    # 显示图表
    plt.show()

# 示例：使用函数绘制图像
with open(sys.argv[1], 'r') as f:
    ps = []
    for line in f:
        ps.append(tuple(map(float, line.strip().split()[:3])))
    d3(ps)

```


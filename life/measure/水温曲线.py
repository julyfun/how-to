import numpy as np
from matplotlib import pyplot as plt

# 室温 20 度，白色小亚克力容器
d = np.array([
    (0, 73.4),
    (1, 71.4), (2, 69.3), (2.5, 68.3), (3, 67.1), (3.5, 66.3), (4, 65.5), (4.5, 64.5), (5, 63.6), (5.5, 63.1), (6, 62.5), (6.5, 61.5),
    (10, 57.0),
    (64, 31.3),
    (80, 28.4),
])
plt.plot(d[:, 0], d[:, 1])
plt.show()


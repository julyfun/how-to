---
title: deque
date: 2024-11-09 20:20:04
tags: ["langs", "python", "collections"]
---
# deque

```
from collections import deque

# 创建一个空的 deque
d = deque()

# 从右侧添加元素
d.append(1)

# 从左侧添加元素
d.appendleft(0)

# 从右侧移除元素
d.pop()  # 返回 2

# 从左侧移除元素
d.popleft()  # 返回 0

# 指定最大长度的 deque
d = deque(maxlen=3)
d.extend([1, 2, 3])
d.append(4)  # 超过后，左侧元素会被移除
print(d)  # 输出: deque([2, 3, 4], maxlen=3)

# 反转队列
d.reverse()
print(d)  # 输出: deque([4, 3, 2])

# 旋转队列
d.rotate(1)  # 向右旋转
print(d)  # 输出: deque([2, 4, 3])
d.rotate(-1)  # 向左旋转
print(d)  # 输出: deque([4, 3, 2])
```


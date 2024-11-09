n = int(input())
x, y, p = [], [], []
for _ in range(n):
    x1, y1, p1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
    p.append(p1)

from collections import deque


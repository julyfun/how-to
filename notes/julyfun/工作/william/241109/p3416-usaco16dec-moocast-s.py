n = int(input())
e = [[] for _ in range(n)]
pos, p = [], []
for _ in range(n):
    x1, y1, p1 = map(int, input().split())
    pos.append((x1, y1))
    p.append(p1)

def dis(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    
for i in range(n): 
    for j in range(n):
        if i == j: continue
        if dis(pos[i], pos[j]) <= p[i] ** 2:
            e[i].append(j)

from collections import deque
ans = 0
for i in range(n):
    # 开启 bfs
    vis = [False] * n
    q = deque()
    q.append(i)
    tot = 0
    vis[i] = True
    while len(q) > 0:
        tot += 1
        u = q.popleft()
        for v in e[u]:
            if not vis[v]:
                q.append(v)
    if tot > ans:
        ans = tot
print(ans)


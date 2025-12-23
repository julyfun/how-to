def dfs(u, fa, k, depth=0):
    global cnt
    for v, w in G[u]:
        if v != fa and w >= k:
            cnt += 1
            dfs(v, u, k, depth + 1)

import sys
# sys.stdin = open('/Users/florian/Downloads/P6111_8.in', 'r')
# Increase the recursion limit
sys.setrecursionlimit(10000)

n, Q = map(int, input().split())
G = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, q, r = map(int, input().split())
    G[p].append((q, r))
    G[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    cnt = 0
    dfs(v, -1, k)
    print(cnt)


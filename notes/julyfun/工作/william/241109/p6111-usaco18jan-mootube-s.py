def dfs(u, fa, k):
    global cnt
    for v, w in G[u]:
        if v != fa and w >= k:
            cnt += 1
            dfs(v, u, k)

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


n = int(input())
f = [[0, 0] for _ in range(n)]
v = [[0, 0] for _ in range(n)]
for i in range(n):
    s = list(map(int, input().split()))
    for j, x in enumerate(s):
        f[j][(i + 1) % 2] += x
        v[i][(j + 1) % 2] += x

ans1 = 0
for x, y in f:
    ans1 += max(x, y)
ans2 = 0
for x, y in v:
    ans2 += max(x, y)
print(max(ans1, ans2))



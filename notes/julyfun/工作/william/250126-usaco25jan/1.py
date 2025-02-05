n = int(input())
a = list(map(int, input().split()))
pa = dict()
for i, v in enumerate(a):
    pa[v] = pa.get(v, []) + [i]
b = list(map(int, input().split()))
ans = 0
pb = dict()
for i, v in enumerate(b):
    pb[v] = pb.get(v, []) + [i]
    for i2 in pa.get(v, []):
        x, y = min(i, i2), max(i, i2)
        ans += min(x + 1, n - y)
        if x == y:
            ans += (x + 1) * x // 2 # at 1 => 0 ~ 0 => 2 * 1 / 2
            ans += (n - y) * (n - y - 1) // 2 # at n - 2
 
print(ans)


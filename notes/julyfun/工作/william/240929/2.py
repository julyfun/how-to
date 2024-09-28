n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
t = 0
minans = 1e9
for s in range(n):
    while t + 1 <= n - 1 and a[t + 1] - a[s] + 1 <= n:
        t += 1
    minans = min(minans, n - (t - s + 1))
print(minans)
totdis = a[n - 1] - a[0] - (n - 1)
print(totdis - min(a[2] - a[1], a[n - 1] - a[n - 2]) + 1)
    

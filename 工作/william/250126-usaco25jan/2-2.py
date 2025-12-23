def cal(L, R, x, a, prefix):
    return ((x - L) * a[x] - (prefix[x - 1] - prefix[L - 1])) + (prefix[R] - prefix[x] - (R - x) * a[x])

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x % m for x in a]
    a.sort()
    
    a = [0] + a + [m + x for x in a] + [2 * m + x for x in a]
    
    prefix = [0] * (3 * n + 1)
    for i in range(1, 3 * n + 1):
        prefix[i] = prefix[i - 1] + a[i]
    
    L, R = 2, n + 1
    ans = int(1e18)
    for i in range(n + 1, 2 * n + 1):
        while R < 3 * n and (R < i or cal(L, R, i, a, prefix) >= cal(L + 1, R + 1, i, a, prefix)):
            L += 1
            R += 1
        ans = min(ans, cal(L, R, i, a, prefix))
    
    print(ans)


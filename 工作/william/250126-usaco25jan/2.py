t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted([x % m for x in map(int, input().split())])
    p1, p2 = 0, n - 1 # [p1, p2] closer to a[p]
    p = n - 1
    for i, v in enumerate(a):
        if a[p] - v <= v - (a[p] - m):
            p1 = i
            break
    cur = sum([min(a[p] - v, v - (a[p] - m)) for v in a])
    ans = cur
    # print(f"cur: {cur}, a: {a}")
    while p > 0:
        # a[p] => a[p - 1]
        # a[p] - m, a[p], a[p] + m
        pp1 = p1
        # p1 - 1: a[p] - m => a[p - 1]
        while p1 > 0 and a[p - 1] - a[p1 - 1] <= a[p1 - 1] - (a[p - 1] - m):
            cur -= a[p1 - 1] - (a[p] - m)
            cur += a[p - 1] - a[p1 - 1]
            p1 -= 1
        pp2 = p2
        # p2 - 1: a[p] => a[p - 1] + m
        while p2 > p - 1 and a[p - 1] + m - a[p2 - 1] <= a[p2 - 1] - a[p - 1]:
            cur -= a[p2 - 1] - a[p]
            cur += a[p - 1] + m - a[p2 - 1]
            p2 -= 1
        move = a[p] - a[p - 1]
        cur += p1 * move
        cur -= (p - 1 - pp1) * move
        cur += (p2 - p) * move
        cur -= (n - 1 - pp2) * move
        ans = min(ans, cur) 
        # print(f"p: {p}, p1: {p1}, p2: {p2}, cur: {cur}")
        p -= 1
    print(ans)

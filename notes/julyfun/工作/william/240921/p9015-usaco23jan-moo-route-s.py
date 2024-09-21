n = int(input())
a = list(map(int, input().split())) + [0]
s = sum(a)
p = 0
d = 1
for _ in range(s):
    if (d == 1 and a[p] == 0) or (d == -1 and a[p - 1] <= 2 and a[p] > 0):
        d = -d
    if d == 1:
        print("R", end='')
        a[p] -= 1
    else:
        print("L", end='')
        a[p - 1] -= 1
    p += d


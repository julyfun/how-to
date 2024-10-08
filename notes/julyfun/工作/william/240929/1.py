N = int(5e6)
once = [True] * (N + 1) 
prime = []
for i in range(2, N + 1):
    if once[i]:
        prime.append(i)
    for j in range(len(prime)):
        v = prime[j]
        if v * i > N:
            break
        once[v * i] = False
        if i % v == 0:
            break
m3 = 3 # largest i: 4i + 3 prime
m1 = 1
towin = [0, 1, 1, 1] + [0] * int(N + 10)
for i in range(4, int(N + 1)):
    if i % 2 == 0:
        towin[i] = i // 2
    elif i % 4 == 1:
        if once[i]:
            m1 = i
            towin[i] = 1
        else:
            towin[i] = (i - m1) // 2 + 1
    elif i % 4 == 3:
        if once[i]:
            m3 = i
            towin[i] = 1
        else:
            towin[i] = (i - m3) // 2 + 1

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    firstmin = 1e9
    win = 0
    for i in range(1, n + 1):
        rd = towin[a[i]] // 2 + 1
        if rd < firstmin:
            firstmin = rd
            win = towin[a[i]] % 2
    if win == 1:
        print("Farmer John")
    else:
        print("Farmer Nhoj")


def once(n):
    if n == 1:
        return True
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True
    
m3 = 0 # largest i: 4i + 3 prime
m1 = 0
towin = [0, 1, 1, 1] + [0] * int(5e6 + 10)
for i in range(4, int(5e6 + 1)):
    if i % 4 == 0:
        towin[i] = i / 2
    if i % 4 == 1:
        towin[i] = 

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))


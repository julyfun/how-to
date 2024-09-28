## Circular Barn

https://usaco.org/index.php?page=viewproblem2&cpid=1255

首先考虑一个房间内如果一直拿，谁会赢。从 1 开始推导，发现当数量为 4k 时，后手赢，其他先手赢。

需要拿几次可以取完？如果后手赢，那么先手要尽可能让对方赢所需拿的次数多一点。如果先手赢，每个房间遵循尽快赢的策略。

有，若偶数，则次数为 i // 2，否则若为 4k + 1，则取最大质数满足取完后为 4k，而 4k + 3 类似:

```py
    if i % 2 == 0:
        towin[i] = i / 2
    elif i % 4 == 1:
        if once[i]:
            m1 = i
            towin[i] = 1
        else:
            towin[i] = (i - m1) / 2 + 1
    elif i % 4 == 3:
        if once[i]:
            m3 = i
            towin[i] = 1
        else:
            towin[i] = (i - m3) / 2 + 1
```

首先用质数筛筛出质数。对于取完次数为 k 的房间，需要第 k / 2 + 1 轮到这个房间才能有人输。

```py
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
```
## Sleepy Cow Herding

https://usaco.org/index.php?page=viewproblem2&cpid=918

最少的步数：假设最后所有奶牛集中到 p ~ q，显然有 `a[0] <= p < q <= a[n - 1]`，长度为 n，那么发现任意指定一个 p ~ q，每一步都可以把一头在外面的奶牛移进来。只需要双指针法找到长度为 n 的包含奶牛个数最多的区间就行。

最多的步数：定义总距离为每对相邻奶牛之间距离 - 1 的和。如果边缘有两头奶牛相邻，发现每步一定可以只让距离减 1，而第一步一定会把两端移到中间某个位置，故最优方案就是两端先造成一个相邻，之后不断减 1

## 作业题:

## COW Operations

https://usaco.org/index.php?page=viewproblem2&cpid=1232

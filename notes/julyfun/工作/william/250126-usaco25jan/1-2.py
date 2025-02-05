def get_sum(u):
    return u * (u + 1) // 2


n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
loc1 = [[] for _ in range(n + 1)]
loc2 = [[] for _ in range(n + 1)]
ans = 0

for i in range(1, n + 1):
    loc1[a[i]].append(min(i, n - i + 1))

for i in range(1, n + 1):
    loc2[b[i]].append(min(i, n - i + 1))

for i in range(1, n + 1):
    loc1[i].sort()
    loc2[i].sort()

    len1 = len(loc1[i]) - 1
    len2 = len(loc2[i]) - 1
    k = 0
    sum_val = 0
    for j in range(len1 + 1):
        while k <= len2 and loc1[i][j] > loc2[i][k]:
            sum_val += loc2[i][k]
            k += 1
        ans += sum_val + (len2 - k + 1) * loc1[i][j]

for i in range(1, n + 1):
    if a[i] == b[i]:
        ans += get_sum(i - 1) + get_sum(n - i)

print(ans)


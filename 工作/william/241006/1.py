  k = 6
0 1 2 3 4 5 6 7 8 9 10
                 
  1 1 0 0 1 0 0 0 1 1
      l         r = l + k - 1
求区间和:  前缀和
  1 2 2 2 3 3 3 3 4 4
pre[i] = 1 ~ i 有几个坏灯
l ~ r 有几个坏灯，怎么用 pre 数组表示
pre[r] - pre[l - 1]

伪代码:
读入 n, k, b
a 为长度 n + 1 的全 0 数组
把坏灯位置读入:
    读入一个坏灯 x
    a[x] += 1
a 数组做前缀和:
for i in range(1, n + 1):
    a[i] += a[i - 1]
# l + k - 1 <= n
# l <= n + 1 - k
ans =int( 1e9)
for 左端点 l in range(1, n + 2 - k):
    r = l + k - 1
    if 坏灯数量 a[r] - a[l - 1] < ans:
        ans = a[r] - a[l - 1]
输出 ans


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = dict()
for l in a:
    for x in l:
        cnt[x] = cnt.get(x, 0) + 1
for k, v in cnt.items():
    print(k, v)
    

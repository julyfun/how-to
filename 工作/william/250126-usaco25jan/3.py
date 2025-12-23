n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

cnt = dict()
for l in a:
    for x in l:
        cnt[x] = cnt.get(x, 0) + 1

# 找到出现单次所在行。单次对应尽可能是 2 or 2 * n，剩下全部确定
to_ori = dict()
for l in a:
    ok = False
    for x in l:
        if cnt[x] == 1:
            ok = True
            # 假设对应 2. 两次对应 3，三次对应 4...
            for x in l:
                to_ori[x] = cnt[x] + 1
            for x in range(2, 2 * n + 1):
                if x not in to_ori:
                    to_ori[x] = 2 * n + 2 - (cnt[x] + 1)
    if ok:
        break
    
m = tuple([tuple([to_ori[x] for x in l]) for l in a])
m2 = tuple([tuple([2 * n + 2 - x for x in l]) for l in m])
m = min(m, m2)
for l in m:
    for x in l:
        print(x, end=' ')
    print()


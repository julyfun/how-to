n = int(input())
s = input()
p = list(map(int, input().split()))
p = [(x - 1) for x in p]
fh, fg = -1, -1
lh, lg = -1, -1
for i in range(n):
    if s[i] == 'H':
        lh = i
        if fh == -1:
            fh = i
    else:
        lg = i
        if fg == -1:
            fg = i
ans = 0
# GGHH ; G + H 必须 H 包含所有 H
if p[fh] >= lh: # fh and some g before that
    for i in range(fh):
        if p[i] >= fh or (i == 0 and p[i] >= lg):
            ans += 1
if p[fg] >= lg:
    for i in range(fg):
        if p[i] >= fg or (i == 0 and p[i] >= lh):
            ans += 1
print(ans)


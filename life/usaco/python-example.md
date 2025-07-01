---
title: python-example
date: 2024-02-03 00:08:03
tags: ["life", "usaco"]
---
ref: https://blog.csdn.net/m0_37966618/article/details/80374581

```
"""
ID: ***
LANG: PYTHON3
TASK: wormhole
"""
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
N = int(fin.readline())
total_List = list()
def checkPairings(listGenrt,crd):
    for i in range(len(crd)):#assign starting point
        sPt = crd[i]
        lG = list(listGenrt)
        org = list(sPt)
        nXt = []
        num = 0
        while(True):#checking solutions of this starting point
            for tpl in listGenrt:
                if sPt in tpl:
                    sPt = tpl[0 if tpl.index(sPt) == 1 else 1]
                    if tpl in lG:
                        lG.remove(tpl)
 
            for x in crd:
                if x[1] == sPt[1] and x != sPt and x[0] > sPt[0]:
                    if nXt==[] or (nXt!=[] and x[0] < nXt[0]):
                        nXt =  x
 
            if(nXt==[]):#can't find wh with the same Y value
                break
            sPt = list(nXt)
            nXt = []
            if sPt == org and len(lG)!=len(listGenrt):
                num+=1
                break
 
        if num!=0:
            total_List.append(listGenrt)
            break
   
def createPairings(remaining):
    if len(remaining)==0:
        return
 
    for x in range(1,len(remaining)):
        if(x>1):
            P2 = list(pairings)
            #print("---{}".format(P2))
            checkPairings(P2,crd)
 
            del pairings[(len(P2)-int(len(remaining)/2)):len(P2)]
 
        pairings.append((remaining[0], remaining[x]))
        p = list(remaining)
        p.pop(0)
        p.pop(x-1)
        createPairings(p)
        if(x==len(remaining)-1 and len(pairings)==len(remaining)/2):
            checkPairings(pairings,crd)
 
crd = list()
pairings = list()
for x in range(N):
    c = list(map(int,fin.readline().split()))
    crd.append(c)
#print(crd)
createPairings(crd)
fout.write("{}\n".format(str(len(total_List))))
fout.close()
```

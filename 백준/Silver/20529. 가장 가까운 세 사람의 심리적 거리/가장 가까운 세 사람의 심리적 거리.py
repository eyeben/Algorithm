from collections import defaultdict
from itertools import combinations
for _ in range(int(input())):
    N = int(input())
    li = input().split()
    dd = defaultdict(int)
    for itm in li:
        dd[itm] = min(3, dd[itm] + 1)
    li2 = []
    for itm in dd.keys():
        for _ in range(dd[itm]):
            li2.append(itm)
    comb = list(combinations(li2, 3))
    ans = 100
    for itm in comb:
        tmp = 0
        for i in range(4):
            tmp += (itm[0][i] != itm[1][i]) + (itm[0][i] != itm[2][i]) + (itm[1][i] != itm[2][i])
        ans = min(ans, tmp)
    print(ans)
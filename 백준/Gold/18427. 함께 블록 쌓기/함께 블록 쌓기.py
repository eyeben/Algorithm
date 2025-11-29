from collections import defaultdict
N, M, H = map(int, input().split())
li = [[0] + list(map(int, input().split())) for _ in range(N)]

dd = defaultdict(int)
for itm in li[0]:
    dd[itm] = 1

for itms in li[1:]:
    dd2 = defaultdict(int)
    for itm in itms:
        for k in dd.keys():
            if k + itm <= H:
                dd2[k + itm] = (dd2[k + itm] + dd[k]) % 10_007
    dd = dd2

print(dd[H])

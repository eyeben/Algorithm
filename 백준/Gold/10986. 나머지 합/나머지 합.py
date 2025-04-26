from collections import defaultdict
N, M = map(int,input().split())

li = list(map(int,input().split()))
nu = [li[0] % M]
for i in range(1, N):
    nu.append((nu[-1]+li[i]) % M)

dd = defaultdict(int)

for itm in nu:
    dd[itm] += 1

cnt = dd[0]
for k in dd.keys():
    getsu = dd[k]
    if getsu >= 2:
        cnt += getsu*(getsu-1)//2
print(cnt)
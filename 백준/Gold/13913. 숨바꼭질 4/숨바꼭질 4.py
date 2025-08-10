from collections import deque
N, K = map(int, input().split())
dic = dict()
BIG = int(1e9)
li = [BIG] * (200_000)

dq = deque([N])
li[N] = 0

while dq:
    n = dq.popleft()
    for itm in [n - 1, n + 1, 2 * n]:
        if 0 <= itm < 200_000 and li[n] + 1 < li[itm]:
            li[itm] = li[n] + 1
            dic[itm] = n
            dq.append(itm)
    if li[K] != BIG:
        break
anss = [K]
tmp = K
while tmp in dic:
    anss.append(dic[tmp])
    tmp = dic[tmp]
anss.reverse()

print(li[K])
print(*anss)
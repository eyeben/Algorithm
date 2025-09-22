from collections import deque, defaultdict
N, M = map(int, input().split())
li = list(map(int, input().split()))

dd = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    dd[a] += b


adjs = [[] for _ in range(N + 1)]
for i in range(1, N):
    adjs[li[i]].append(i + 1)

ans = [0] * (N+1)
kys = sorted(dd.keys())
dq = deque([(1, dd[1])])
ans[1] = dd[1]
while dq:
    emp, comp = dq.popleft()
    for itm in adjs[emp]:
        dq.append((itm, comp + dd[itm]))
        ans[itm] += comp + dd[itm]
print(*ans[1:])


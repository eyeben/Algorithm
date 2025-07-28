import heapq
from collections import defaultdict
N = int(input())
dd = defaultdict(list)
mx = 0
for _ in range(N):
    a, b = map(int, input().split())
    mx = max(a, mx)
    dd[a].append(b)

hq = []
ans = 0
for i in range(mx,0,-1):
    for itm in dd[i]:
        heapq.heappush(hq, -itm)
    if hq:
        ans -= heapq.heappop(hq)
print(ans)


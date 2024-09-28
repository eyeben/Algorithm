import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
N = int(input())

counts = defaultdict(list)

for _ in range(N):
    a,b = map(int,input().split())
    counts[a].append(b)

ans = 0
hq = []
for day in range(N,0,-1):
    if day in counts:
        for itm in counts[day]:
            heapq.heappush(hq, -itm)
    if hq:
        ans += -heapq.heappop(hq)
print(ans)
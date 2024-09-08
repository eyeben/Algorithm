import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

indegree = [0]* (N+1)
adjs = [[] for _ in range(N+1)]


for _ in range(M):
    a,b = map(int, input().split())
    adjs[a].append(b)
    indegree[b] += 1

hq = []

for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)

ans = []
while hq:
    node = heapq.heappop(hq)
    ans.append(node)
    for itm in adjs[node]:
        indegree[itm] -= 1
        if indegree[itm] == 0:
            heapq.heappush(hq, itm)

print(*ans)
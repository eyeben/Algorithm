import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = defaultdict(list)
indegree = [0]*(N+1)
for _ in range(M):
    a,b = map(int, input().split())
    indegree[b] += 1
    dic[a].append(b)

hq = []
anss = []
for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)

while hq:
    tmp = heapq.heappop(hq)
    anss.append(str(tmp))

    if tmp in dic:
        for itm in dic[tmp]:
            indegree[itm] -= 1
            if indegree[itm] == 0:
                heapq.heappush(hq,itm)
print(' '.join(anss))
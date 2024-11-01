import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
BIG = 9999999
def dijkstra(start):
    distance = [BIG] * (N+1)
    hq = []
    heapq.heappush(hq, (0,start))
    #distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)

        if distance[node] < dist:
            continue

        distance[node] = dist

        for node2, dist2 in adj[node]:
            if dist + dist2 < distance[node2]:
                distance[node2] = dist + dist2
                heapq.heappush(hq,(distance[node2], node2))
    cnt, maxi = 0, 0
    for itm in distance:
        if itm != BIG:
            cnt += 1
            maxi = max(maxi, itm)
    print(cnt, maxi)


for T in range(int(input())):
        
    N, M, start = map(int,input().split())


    adj = defaultdict(list)
    for i in range(M):
        a,b,c = map(int, input().split())
        adj[b].append((a,c))
    dijkstra(start)




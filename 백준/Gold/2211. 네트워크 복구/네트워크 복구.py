import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
li = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    li[a].append((b, c))
    li[b].append((a, c))


BIG = 1e9
def dijk(start):
    dists = [BIG]*(N+1)
    dists[start] = 0
    connections = [0]*(N+1)
    hq = [(0,start)]
    while hq:
        dist, node = heapq.heappop(hq)
        if dists[node] < dist:
            continue
        for nextNode, length  in li[node]:
            if dists[nextNode] > dist + length:
                connections[nextNode] = node
                dists[nextNode] = dist + length
                heapq.heappush(hq, (dist + length, nextNode))
    print(N-1)
    for i in range(2,N+1):
        print(i, connections[i])

dijk(1)
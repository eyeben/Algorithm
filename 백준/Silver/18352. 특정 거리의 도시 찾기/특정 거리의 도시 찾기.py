import heapq
import sys

input = sys.stdin.readline

N,M,K,X = map(int, input().split())

li = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    li[a].append(b)

def dijk(S):
    dists = [1e9]*(N+1)
    dists[S] = 0

    hq = [(0,S)]

    while hq:
        dist, node = heapq.heappop(hq)
        if dists[node] < dist:
            continue

        for nextNode in li[node]:
            if dists[nextNode] > dist+1:
                heapq.heappush(hq, (dist+1, nextNode))
                dists[nextNode] = dist+1

    badFlag = True
    for i in range(1,N+1):
        if K == dists[i]:
            badFlag = False
            print(i)
    if badFlag:
        print(-1)
dijk(X)
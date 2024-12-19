from collections import deque
N = int(input())
M = int(input())
li = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    li[a-1].append((b-1, c))

S, E = map(int, input().split())
S -= 1
E -= 1

BIG = int(1e9)

dists = [BIG]*N
route = [[] for _ in range(N)]
dists[S] = 0
route[S] = [S]
dq = deque()
dq.append((S,0))

while dq:
    node, dist = dq.popleft()
    if dists[node] < dist:
        continue
    for nextNode,nextDist in li[node]:
        if dist + nextDist < dists[nextNode]:
            dists[nextNode] = dist + nextDist
            route[nextNode] = route[node] + [nextNode]
            dq.append((nextNode, dist + nextDist))
print(dists[E])
print(len(route[E]))
for itm in route[E]:
    print(itm+1, end = ' ')
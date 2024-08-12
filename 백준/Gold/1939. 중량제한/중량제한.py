import sys
from collections import deque


def bfs(weight):
    que = deque([S])
    visited = [False]*(N+1)
    visited[S] = True

    while que:
        x = que.popleft()
        for y, z in adj[x]:
            if not visited[y] and z >= weight:
                visited[y] = True
                que.append(y)
    if visited[E]:
        return True
    else:
        return False


N, M = map(int,input().split())
adj = [[] for _ in range(N + 1)]
weights = set()

for _ in range(M):
    x,y,weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    weights.add(weight)




S, E = map(int,input().split())

weights = sorted(list(weights))
piv1 = 0
piv2 = len(weights) - 1

while piv1<=piv2:
    piv = (piv1+piv2)//2
    if(bfs(weights[piv])):
        ans = piv
        piv1 = piv + 1
    else:
        piv2 = piv - 1

print(weights[ans])
from collections import deque
N = int(input())
li = [[] for _ in range(N+1)]
while 1:
    a,b = map(int,input().split())
    if a == -1 and b ==-1:
        break
    li[a].append(b)
    li[b].append(a)

bd = [0]
def bfs(s):
    visited = [0]*(N+1)
    visited[s] = -1
    dq = deque()
    dq.append((s,0))
    while dq:
        node, dist = dq.popleft()
        for itm in li[node]:
            if not visited[itm]:
                visited[itm] = dist+1
                dq.append((itm, dist+1))
    visited[s] = 0
    return max(visited)


for i in range(1,N+1):
    bd.append(bfs(i))
mn = min(bd[1:])
ans = []
for i in range(1,N+1):
    if mn == bd[i]:
        ans.append(i)
print(mn,len(ans))
for itm in ans:
    print(itm,end = ' ')
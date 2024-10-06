import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
li = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    li[b].append(a)

anss = [0]*(N+1)
for i in range(1, N+1):
    visited = [False]*(N+1)
    visited[i] = True
    dq = deque([i])
    cnt = 1
    while dq:
        n = dq.popleft()

        for itm in li[n]:
            if not visited[itm]:
                cnt+=1
                visited[itm] = True
                dq.append(itm)
    anss[i] = cnt

mx = max(anss)
ans = []
for i in range(1,N+1):
    if mx == anss[i]:
        ans.append(i)


print(*ans)
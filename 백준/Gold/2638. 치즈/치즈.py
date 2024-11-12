import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
li = []
cnt = 0
for _ in range(N):
    li.append(list(map(int, input().split())))
    cnt += sum(li[-1])

dx = [0,1,0,-1]
dy = [1,0,-1,0]



def bfs(sx,sy):
    global cnt
    popList = []
    visited = [[False] * M for _ in range(N)]
    isAir = [[False]*M for _ in range(N)]

    adq = deque()
    isAir[sy][sx] = True
    adq.append((sx, sy))
    while adq:
        x,y = adq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0 <= nx < M and 0 <= ny < N) or isAir[ny][nx]:
                continue
            if li[ny][nx] == 0:
                isAir[ny][nx] = True
                adq.append((nx,ny))


    dq = deque()
    visited[sy][sx] = True
    dq.append((sx,sy))

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if not(0<=nx<M and 0<=ny<N) or visited[ny][nx]:
                continue
            if li[ny][nx] == 1:
                byunCnt = 0
                for j in range(4):
                    nx2, ny2 = nx + dx[j], ny + dy[j]
                    if isAir[ny2][nx2]:
                        byunCnt += 1
                if byunCnt >= 2:
                    popList.append((nx, ny))
            else:
                dq.append((nx, ny))
            visited[ny][nx] = True

    cnt -= len(popList)
    for x,y in popList:
        li[y][x] = 0

ans = 0
while cnt:
    bfs(0,0)
    ans += 1

print(ans)
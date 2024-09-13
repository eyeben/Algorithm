from collections import deque
BIG = 1e9
N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if li[i][j] == 1:
            li[i][j] = -1

dx = [0,1,0,-1]
dy = [-1,0,1,0]
def bfs(sx,sy,num):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append((sx,sy))
    visited[sy][sx] = True
    li[sy][sx] = num

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<= nx<N and 0<= ny < N:
                if not visited[ny][nx] and li[ny][nx] == -1:
                    visited[ny][nx] = True
                    li[ny][nx] = num
                    q.append((nx,ny))

islandNum = 1
for i in range(N):
    for j in range(N):
        if li[i][j] == -1:
            bfs(j,i,islandNum)
            islandNum += 1
islandNum -= 1

adjs = [[BIG]*(islandNum+1) for _ in range(islandNum+1)]

def makeBridges(sx,sy):
    start = li[sy][sx]
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append((sx, sy, 0))
    visited[sy][sx] = True
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx<N and 0<=ny<N:
                if visited[ny][nx]:
                    continue
                if li[ny][nx] == start:
                    continue
                if li[ny][nx] != 0:
                    end = li[ny][nx]
                    adjs[start][end] = adjs[end][start] = min(dist,adjs[start][end], adjs[end][start])
                else:
                    q.append((nx, ny, dist + 1))
                visited[ny][nx] = True

for i in range(N):
    for j in range(N):
        if li[i][j]:
            makeBridges(j,i)

mini = BIG
for itms in adjs:
    mini = min([mini]+itms)
print(mini)
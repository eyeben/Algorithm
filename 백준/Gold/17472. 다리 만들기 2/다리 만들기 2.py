from collections import deque

R, C = map(int, input().split())
bd = []
for _ in range(R):
    bd.append(list(map(int, input().split())))

for i in range(R):
    for j in range(C):
        if bd[i][j]:
            bd[i][j] = -1

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfsMark(sx,sy,label):
    dq = deque()
    dq.append((sx,sy))
    bd[sy][sx] = label
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < C and 0<= ny < R and bd[ny][nx] == -1:
                bd[ny][nx] = label
                dq.append((nx,ny))

islandCnt = 1
for i in range(R):
    for j in range(C):
        if bd[i][j] == -1:
            bfsMark(j, i, islandCnt)
            islandCnt += 1
islandCnt -= 1

BIG = 10
distances = [[BIG]*(islandCnt+1) for _ in range(islandCnt+1)]

def createBridge(sx,sy):
    if bd[sy][sx] == 0:
        return

    for i in range(4):
        nx, ny = sx+dx[i], sy+dy[i]
        length = 0
        while 0<= nx < C and 0<= ny < R and bd[ny][nx] == 0:
            nx += dx[i]
            ny += dy[i]
            length += 1
        if length >= 2 and 0<= nx < C and 0<= ny < R:
            label1, label2 = bd[sy][sx], bd[ny][nx]
            length = min(length, distances[label1][label2])
            distances[label1][label2] = length
            distances[label2][label1] = length

for i in range(R):
    for j in range(C):
        createBridge(j,i)

listOfDistancse = []
for i in range(1, islandCnt):
    for j in range(i+1, islandCnt + 1):
        if distances[i][j] != BIG:
            listOfDistancse.append((distances[i][j], i, j))

parents = [i for i in range(islandCnt+1)]

def findParent(a):
    while a != parents[a]:
        a = parents[a]
    return a

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parents[b] = a
    elif a > b:
        parents[a] = b

listOfDistancse.sort()
ans = 0
for dist, a, b in listOfDistancse:
    if findParent(a) == findParent(b):
        continue
    union(a,b)
    ans += dist

rootParent = findParent(1)
for i in range(1,islandCnt+1):
    if rootParent != findParent(i):
        print(-1)
        exit(0)

print(ans)
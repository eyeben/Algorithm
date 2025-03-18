import heapq
W, H = map(int, input().split())
bd = []
for _ in range(H):
    bd.append(input())

cs = []
for i in range(H):
    for j in range(W):
        if bd[i][j] == 'C':
            cs.append([j,i])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

BIG = int(1e9)
dists = [[[BIG]*4 for _ in range(W)] for _ in range(H)]
sx,sy = cs[0][0],cs[0][1]
ex, ey = cs[1][0], cs[1][1]

dists[sy][sx][0] = dists[sy][sx][1]= dists[sy][sx][2] = dists[sy][sx][3] = 0
hq = []
heapq.heappush(hq, (0, sx, sy, 0))
heapq.heappush(hq, (0, sx, sy, 1))
heapq.heappush(hq, (0, sx, sy, 2))
heapq.heappush(hq, (0, sx, sy, 3))
paths = []

while hq:
    d, x, y, direction = heapq.heappop(hq)
    if dists[y][x][direction] < d:
        continue
    for i in range(4):
        nx, ny, nd = x+dx[i], y+dy[i], d
        if 0<= nx < W and 0<=ny<H and not bd[ny][nx] == '*':
            if i != direction:
                nd += 1
            if dists[ny][nx][i] > nd:
                dists[ny][nx][i] = nd
                heapq.heappush(hq,(nd, nx, ny, i))

print(min(dists[ey][ex]))

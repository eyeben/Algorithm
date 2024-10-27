import sys
import heapq
input = sys.stdin.readline
N = int(input())
bd = []
for i in range(N):
    bd.append(list(input().strip()))

BIG = 1e9
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dijk(sx, sy):
    dists = [[BIG]*N for _ in range(N)]
    dists[sy][sx] = 0
    hq = [(0,sx,sy)]

    while hq:
        dist, x, y = heapq.heappop(hq)
        if dists[y][x] < dist:
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<N and 0<=ny<N):
                continue
            ndist = dist
            if bd[ny][nx] == '0':
                ndist += 1
            if dists[ny][nx] > ndist:
                dists[ny][nx] = ndist
                heapq.heappush(hq, (ndist, nx,ny))
    print(dists[-1][-1])

dijk(0,0)





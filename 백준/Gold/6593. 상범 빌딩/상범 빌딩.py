import heapq
import sys
input = sys.stdin.readline

BIG = 1e9


dx = [0,1,0,-1, 0, 0,]
dy = [-1, 0,1, 0, 0,0]
dz = [0, 0, 0, 0,1,-1]


def dijk(sx,sy,sz, ex,ey,ez):
    distances = [[[BIG] *C for _ in range(R)] for _ in range(L)]
    hq = []
    heapq.heappush(hq,[0,sx,sy,sz])
    distances[sz][sy][sx] = 0

    while hq:
        dist, x,y,z = heapq.heappop(hq)
        if distances[z][y][x] < dist:
            continue
        for i in range(6):
            nx, ny, nz  = x+dx[i],y+dy[i], z+dz[i]
            if 0<= nx< C and 0<= ny < R and 0<= nz<L and li[nz][ny][nx] != '#':
                if distances[nz][ny][nx] > dist + 1:
                    distances[nz][ny][nx] = dist + 1
                    heapq.heappush(hq, [dist + 1, nx,ny,nz])
                    
    return distances[ez][ey][ex]




while(1):
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        exit(0)

    li = [[[] for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            li[i][j] = list(input().strip())
        input()

    sx,sy,sz,ex,ey,ez = -1,-1,-1,-1,-1,-1
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if li[i][j][k] == 'S':
                    sx, sy, sz = k,j,i
                if li[i][j][k] == 'E':
                    ex, ey, ez = k,j,i
                if sx != -1 and ex != -1:
                    break
            if sx != -1 and ex != -1:
                break
        if sx != -1 and ex != -1:
            break

    ans = dijk(sx,sy,sz,ex,ey,ez)
    if ans == BIG:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % ans)

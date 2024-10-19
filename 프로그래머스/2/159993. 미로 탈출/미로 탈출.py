import heapq

BIG = 1e9


def solution(maps):    
    N = len(maps)
    M = len(maps[0])
    
    sx = 0
    sy = 0
    lx = 0
    ly = 0
    ex = 0
    ey = 0
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                sx, sy = j,i
            elif maps[i][j] == 'L':
                lx, ly = j,i
            elif maps[i][j] == 'E':
                ex, ey = j,i
    
        
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    dists = [[BIG]*M for _ in range(N)]
    dists[ly][lx] = 0
    hq = [(0,lx,ly)]
    while hq:
        dist, x, y = heapq.heappop(hq)
        if dist > dists[y][x]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<M and 0<=ny<N):
                continue
            if maps[ny][nx] == 'X':
                continue
            if dist+1 < dists[ny][nx]:
                dists[ny][nx] = dist + 1
                heapq.heappush(hq, (dist+1, nx, ny))

    if dists[sy][sx] == BIG or dists[ey][ex] == BIG:
        return -1
    return dists[sy][sx] + dists[ey][ex]
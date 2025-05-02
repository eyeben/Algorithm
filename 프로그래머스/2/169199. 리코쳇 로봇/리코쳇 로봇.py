import heapq
def solution(board):
    BIG = int(1e9)
    M = len(board[0])
    N = len(board)
    
    RX, RY, GX, GY = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                RX, RY = j, i
            elif board[i][j] == 'G':
                GX, GY = j, i
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dists = [[BIG] * M for _ in range(N)]
    dists[RY][RX] = 0
    hq = [(0, RX, RY)]
    while hq:
        dist, x, y = heapq.heappop(hq)
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx + dx[i] < M and 0 <= ny + dy[i] < N and board[ny+dy[i]][nx+dx[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if nx == x and ny == y:
                continue
            if dists[ny][nx] > dist + 1:
                dists[ny][nx] = dist + 1
                heapq.heappush(hq, (dist+1,nx,ny))
    ans = dists[GY][GX]
    if ans == BIG:
        ans = -1
    
    return ans
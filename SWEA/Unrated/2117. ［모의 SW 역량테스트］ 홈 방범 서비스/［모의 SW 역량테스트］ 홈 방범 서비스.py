from collections import deque

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())

    li = []
    for _ in range(N):
        li.append(list(map(int, input().split())))

    ans = N

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    def bfs(sx,sy,dist):
        cnt = 0
        visited = [[False] * N for _ in range(N)]
        dq = deque()
        dq.append((sx,sy,1))
        visited[sy][sx] = True
        cnt += li[sy][sx]

        while dq:
            x,y,d = dq.popleft()

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if(0<=nx<N and 0<=ny<N and d+1 <= dist and not visited[ny][nx]):
                    cnt += li[ny][nx]
                    visited[ny][nx] = True
                    dq.append((nx,ny,d+1))

        return cnt

    mx = 0
    for dist in range(N+1,0,-1):
        goodFlag = False
        for i in range(N):
            for j in range(N):
                tmpcnt = bfs(j,i,dist)
                if tmpcnt * M >= dist**2 + (dist-1)**2:
                    goodFlag = True
                    mx = max(mx, tmpcnt)
        if goodFlag:
            break
    print("#%d %d" % (tc, mx))



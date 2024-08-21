from collections import deque

while 1:
    bd = []
    dots = [[0,0]]

    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break

    for _ in range(R):
        bd.append(list(input()))
    for i in range(R):
        for j in range(C):
            if bd[i][j] == '*':
                dots.append([j,i])
            elif bd[i][j] == 'o':
                dots[0][0] = j
                dots[0][1] = i

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    def bfs(sx, sy):
        visited = [[0]*C for _ in range(R)]
        visited[sy][sx] = -1
        dq = deque()
        dq.append((sx,sy,0))

        while dq:
            x, y, dist = dq.popleft()
            for i in range(4):
                nx, ny = x+dx[i],y+dy[i]
                if 0<= nx < C and 0<= ny <R and not visited[ny][nx] and bd[ny][nx] != 'x':
                    visited[ny][nx] = dist + 1
                    dq.append((nx,ny,dist+1))
        ans = []
        for x,y in dots:
            ans.append(visited[y][x])
        return ans

    dists = []
    badFlag = False
    for x,y in dots:
        dists.append(bfs(x,y))
        if 0 in dists[-1]:
            badFlag = True
            break
    if badFlag:
        print(-1)
        continue

    mn = 1e9
    dotcnt = len(dots)
    def dfs(dotnum, depth,steps):
        global mn
        if depth == dotcnt - 1:
            mn = min(mn,steps)
            return
        for i in range(dotcnt):
            if not visited[i]:
                visited[i] = True
                dfs(i, depth + 1, steps + dists[dotnum][i])
                visited[i] =False

    visited = [False] * dotcnt
    visited[0] = True
    dfs(0,0,0)
    print(mn)
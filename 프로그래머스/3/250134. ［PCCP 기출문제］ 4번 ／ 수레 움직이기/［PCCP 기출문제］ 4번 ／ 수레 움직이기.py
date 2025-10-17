def solution(maze):
    N = len(maze)
    M = len(maze[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ans = int(1e9)
    visited1 = [[False] * M for _ in range(N)]
    visited2 = [[False] * M for _ in range(N)]
    sx1, sy1, sx2, sy2 = -1, -1, -1, -1
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                sx1, sy1 = j, i
            elif maze[i][j] == 2:
                sx2, sy2 = j, i
    visited1[sy1][sx1] = True
    visited2[sy2][sx2] = True
    
    def dfs(x1,y1,x2,y2,cnt):
        nonlocal ans
        if maze[y1][x1] == 3 and maze[y2][x2] == 4:
            ans = min(ans, cnt)
            return
        if maze[y1][x1] != 3:
            for i1 in range(4):
                nx1, ny1 = x1 + dx[i1], y1 + dy[i1]
                if 0 <= nx1 < M and 0<= ny1 < N and maze[ny1][nx1] != 5 and not visited1[ny1][nx1]:
                    visited1[ny1][nx1] = True
                    if maze[y2][x2] != 4:
                        for i2 in range(4):
                            nx2, ny2 = x2 + dx[i2], y2 + dy[i2]
                            if 0 <= nx2 < M and 0<= ny2 < N and maze[ny2][nx2] != 5 and not visited2[ny2][nx2] and not(nx2 == nx1 and ny2 == ny1) and not(nx1 == x2 and ny1 == y2 and nx2 == x1 and ny2 == y1):
                                visited2[ny2][nx2] = True
                                dfs(nx1, ny1, nx2, ny2, cnt + 1)
                                visited2[ny2][nx2] = False
                    elif not(nx1 == x2 and ny1 == y2):
                        dfs(nx1, ny1, x2, y2, cnt + 1)
                    visited1[ny1][nx1] = False
        else:
            for i2 in range(4):
                nx2, ny2 = x2 + dx[i2], y2 + dy[i2]
                if 0 <= nx2 < M and 0<= ny2 < N and maze[ny2][nx2] != 5 and not(nx2 == x1 and ny2 == y1) and not visited2[ny2][nx2]:
                    visited2[ny2][nx2] = True
                    dfs(x1, y1, nx2, ny2, cnt + 1)
                    visited2[ny2][nx2] = False
    
    dfs(sx1, sy1, sx2, sy2, 0)
    return ans if ans != int(1e9) else 0

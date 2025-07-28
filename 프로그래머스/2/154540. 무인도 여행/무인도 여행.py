from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    print(M)
    visited = [[False]*M for _ in range(N)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    def bfs(x, y):
        dq = deque([(x, y)])
        ret = int(maps[y][x])
        visited[y][x] = True
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and maps[ny][nx] != 'X':
                    ret += int(maps[ny][nx])
                    visited[ny][nx] = True
                    dq.append((nx, ny))
        return ret
    ans = []
    for x in range(M):
        for y in range(N):
            if not visited[y][x] and maps[y][x] != 'X':
                ans.append(bfs(x, y))
    return sorted(ans) if len(ans) > 0 else [-1]
from collections import deque
N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]


def bfs(x, y):
    is_Top = True
    level = li[y][x]
    dq = deque([(x, y)])
    visited[y][x] = True
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if li[ny][nx] == level and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dq.append((nx, ny))
                elif li[ny][nx] > level:
                    is_Top = False
    return is_Top


ans = 0
for x in range(M):
    for y in range(N):
        if not visited[y][x]:
            ans += bfs(x, y)

print(ans)

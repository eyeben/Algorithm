import sys
sys.setrecursionlimit(10**4*25)

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * N for _ in range(N)]

cache = [[0 for _ in range(N)] for _ in range(N)]


def dfs(x, y):
    if not visited[y][x]:
        num = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and li[y][x] < li[ny][nx]:
                num = max(num, dfs(nx, ny))
        cache[y][x] = num + 1
        visited[y][x] = True
    return cache[y][x]


mx = 0
for i in range(N):
    for j in range(N):
        mx = max(mx, dfs(i, j))

print(mx)

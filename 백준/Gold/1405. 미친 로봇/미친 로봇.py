import sys
input = sys.stdin.readline
N, d1, d2, d3, d4 = map(int, input().split())

visited = [[False] * (2 * N + 1) for _ in range(2 * N + 1)]
Sx, Sy = N, N
visited[N][N] = True

dp = [d1/100,d2/100,d3/100,d4/100]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
def dfs(x,y,level,possi):
    global ans
    if level == N:
        ans += possi
        return
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if visited[ny][nx]:
            continue
        visited[ny][nx] = True
        dfs(nx,ny,level+1, possi * dp[i])
        visited[ny][nx] = False

dfs(Sx,Sy,0,1)
print(ans)
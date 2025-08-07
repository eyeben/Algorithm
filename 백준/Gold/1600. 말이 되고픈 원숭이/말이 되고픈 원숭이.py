from collections import deque
K = int(input())
W, H = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(H)]

BIG = int(1e9)
dp = [[[BIG] * (K+1) for _ in range(W)] for _ in range(H)]

dp[0][0][0] = 0
dq = deque([(0,0,0)])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

px = [-2, 2,-1,1,-2,2,-1,1]
py = [-1,-1,-2,-2,1,1,2,2]


while dq:
    x, y, n = dq.popleft()
    cnt = dp[y][x][n]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < W and 0 <= ny < H and not li[ny][nx] and cnt + 1 < dp[ny][nx][n]:
            dp[ny][nx][n] = cnt + 1
            dq.append((nx, ny, n))

    if n < K:
        for i in range(8):
            nx, ny = x + px[i], y + py[i]
            if 0 <= nx < W and 0 <= ny < H and not li[ny][nx] and cnt + 1 < dp[ny][nx][n + 1]:
                dp[ny][nx][n+1] = cnt + 1
                dq.append((nx, ny, n + 1))

ans = min(dp[-1][-1])
print(ans if ans != BIG else -1)

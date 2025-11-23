from collections import deque
BIG = int(1e9)
dx = [2,1,2,1,-2,-1,-2,-1]
dy = [-1,-2,1,2,-1,-2,1,2]
for _ in range(int(input())):
    N = int(input())
    sx, sy = map(int,input().split())
    ex, ey = map(int, input().split())

    dists = [[BIG] * N for _ in range(N)]
    dists[sy][sx] = 0
    dq = deque([(sx, sy, 0)])

    while dq:
        x, y, dist = dq.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and dist + 1 < dists[ny][nx]:
                dq.append((nx, ny,dist + 1))
                dists[ny][nx] = dist + 1
        if dists[ey][ex] != BIG:
            break
    print(dists[ey][ex] if dists[ey][ex] != BIG else -1)

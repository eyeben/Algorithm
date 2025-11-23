from collections import deque
N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,num):
    cnt = 1
    li[y][x] = num
    dq = deque([(x, y)])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and li[ny][nx] == 1:
                li[ny][nx] = num
                cnt += 1
                dq.append((nx, ny))
    return cnt


num = 2
mx = 0
for y in range(N):
    for x in range(M):
        if li[y][x] == 1:
            mx = max(mx, bfs(x,y,num))
            num += 1

print(num - 2)
print(mx)
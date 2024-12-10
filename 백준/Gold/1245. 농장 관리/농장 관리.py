from collections import defaultdict, deque

N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
dic = defaultdict(list)
for y in range(N):
    for x in range(M):
        if li[y][x]:
            dic[li[y][x]].append((x, y))
heights = list(dict(dic).keys())
heights.sort(reverse=True)

cnt = 0

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]


def mark(sx, sy, sh):
    visited = set()
    dq = deque()
    visited.add((sx,sy))
    dq.append((sx, sy, sh))
    while dq:
        x, y, h = dq.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<M and 0<=ny<N and (nx,ny) not in visited and li[ny][nx] and li[ny][nx] <= h:
                visited.add((nx,ny))
                dq.append((nx,ny,li[ny][nx]))

    for x,y in visited:
        li[y][x] = 0



for height in heights:
    for x, y in dic[height]:
        if li[y][x]:
            cnt += 1
            mark(x, y, height)
print(cnt)
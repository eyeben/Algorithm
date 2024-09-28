import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4*25)

N = int(input())
li = []

for _ in range(N):
    li.append(list(map(int, input().split())))
ordered = []
for i in range(N):
    for j in range(N):
        ordered.append((li[i][j],j,i))

ordered.sort(reverse=True)

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dfs(x,y, cnt):
    global mx, visited
    badflag = True

    for i in range(4):
        nx,ny = x+dx[i], y +dy[i]

        if not(0<=nx<N and 0<=ny<N):
            continue
        if visited[ny][nx]:
            continue
        if li[ny][nx] <= li[y][x]:
            continue

        if cache[ny][nx]:
            mx = max(mx, cnt+cache[ny][nx])
            continue

        badflag = False
        visited[ny][nx] = True
        dfs(nx,ny,cnt + 1)
        visited[ny][nx] = False

    if badflag:
        mx = max(mx,cnt)


ans = 0
visited = [[False]* N for _ in range(N)]
cache = [[0] * N for _ in range(N)]

for num, x, y in ordered:
    mx = 0
    visited[y][x] = True
    dfs(x,y,1)
    visited[y][x] = False
    ans = max(ans, mx)
    cache[y][x] = mx


print(ans)
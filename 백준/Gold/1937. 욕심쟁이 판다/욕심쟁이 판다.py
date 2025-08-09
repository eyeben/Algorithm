import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4*25)

N = int(input())
trees = [list(map(int, input().split())) for _ in range(N)]

cache = [[-1] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(x,y):
    # 방문한 노드면 그냥 리턴
    if cache[y][x] != -1: # 방문한 노드는 최대 값을 보장하는가? yee
        return cache[y][x]

    mx = 1
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if trees[y][x] < trees[ny][nx]:
            mx = max(mx, 1+ dfs(nx,ny))

    cache[y][x] = mx # 여기가 DP
    return mx

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i,j))

print(ans)
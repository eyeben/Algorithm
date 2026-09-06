from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(land):
    N = len(land)
    M = len(land[0])
    num = 2
    dd = defaultdict(int)
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    def dfs(n, x, y):
        dd[n] += 1
        land[y][x] = n
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and land[ny][nx] == 1:
                dfs(n, nx, ny)
    
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                cnt = 0
                dfs(num,j,i)
                num += 1
    ans = 0
    for x in range(M):
        sett = {land[y][x] for y in range(N)}
        tmp = [dd[itm] for itm in sett]
        ans = max(sum(tmp), ans)
        
    return ans
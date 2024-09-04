dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(x,y,depth):
    global visited, ans
    goodFlag = False
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and li[y][x] > li[ny][nx]:
            visited[ny][nx] = True
            dfs(nx,ny,depth+1)
            visited[ny][nx] = False
            goodFlag = True

    if not goodFlag:
        ans = max(depth,ans)

for tc in range(1,int(input())+1):
    N,K = map(int, input().split())
    li = []
    for _ in range(N):
        li.append(list(map(int,input().split())))

    mx = 0
    for itms in li:
        mx = max(mx,max(itms))

    tops = []
    for i in range(N):
        for j in range(N):
            if(li[i][j] == mx):
                tops.append((j,i))

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(K+1):
                li[i][j] -= k
                for x,y in tops:
                    if x == j and y == i:
                        continue
                    visited = [[False]*N for _ in range(N)]
                    dfs(x,y,1)
                li[i][j] += k

    print("#%d %d"%(tc,ans))



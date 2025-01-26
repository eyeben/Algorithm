N, K = map(int, input().split())
bd = []
for _ in range(N):
    bd.append(list(map(int, input().split())))


mal = [] # y, x, d
bd2 = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(K):
    y,x,d = map(int, input().split())
    mal.append([y-1,x-1,d-1])
for i in range(K):
    bd2[mal[i][0]][mal[i][1]].append(i)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

for times in range(1000):
    for i in range(K):
        y, x, d = mal[i]

        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < N or not 0 <= ny < N or bd[ny][nx] == 2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
            mal[i][2] = d
            nx, ny = x + dx[d], y + dy[d]
            if not 0 <= nx < N or not 0 <= ny < N or bd[ny][nx] == 2:
                continue


        idx = bd2[y][x].index(i)
        group = bd2[y][x][idx:]
        bd2[y][x] = bd2[y][x][:idx]

        if bd[ny][nx] == 0:
            bd2[ny][nx] += group

        elif bd[ny][nx] == 1:
            group.reverse()
            bd2[ny][nx] += group

        for idx in group:
            mal[idx] = [ny, nx, mal[idx][2]]

        if len(bd2[ny][nx]) >= 4:
            print(times+1)
            exit()
print(-1)
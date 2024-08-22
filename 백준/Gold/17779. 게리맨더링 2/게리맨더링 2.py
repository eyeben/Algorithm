N = int(input())
bd = []
for _ in range(N):
    bd.append(list(map(int, input().split())))

mn = 1e9


def calc(x1, y1, d1, d2):
    global mn
    totals = [0, 0, 0, 0, 0]
    x2, y2 = x1 + d1, y1 - d1
    x3, y3 = x2 + d2, y2 + d2
    x4, y4 = x1 + d2, y1 + d2

    gus = [[-1] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if y < y1 and x <= x2:
                gus[y][x] = 0
            elif y <= y3 and x2 < x:
                gus[y][x] = 1
            elif y >= y1 and x < x4:
                gus[y][x] = 2
            else:
                gus[y][x] = 3
    gus[y1][x1] = gus[y2][x2] = gus[y3][x3] = gus[y4][x4] = 4

    nx, ny = x1, y1
    while nx < x2:
        nx += 1
        ny -= 1
        gus[ny][nx] = 4

    nx, ny = x2, y2
    while nx < x3:
        nx += 1
        ny += 1
        gus[ny][nx] = 4

    nx, ny = x3, y3
    while x4 < nx:
        nx -= 1
        ny += 1
        gus[ny][nx] = 4

    nx, ny = x1, y1
    while nx < x4:
        nx += 1
        ny += 1
        gus[ny][nx] = 4

    for i in range(x1 + 1, x3):
        flag = 0
        for j in range(N):
            if flag == 0 and gus[j][i] == 4:
                flag += 1
            elif flag == 1 and gus[j][i] != 4:
                gus[j][i] = 4
            elif flag == 1 and gus[j][i] == 4:
                break

    for i in range(N):
        for j in range(N):
            totals[gus[i][j]] += bd[i][j]

    mn = min(mn,max(totals) - min(totals))


def dfs(x, y, d1, d2):
    if y - d1 < 0 or y + d2 >= N or x + d1 + d2 >= N or visited[d1][d2]:
        return
    calc(x, y, d1, d2)
    visited[d1][d2] = True
    dfs(x, y, d1 + 1, d2)
    dfs(x, y, d1, d2 + 1)


for i in range(N):
    for j in range(N):
        visited = [[False] * N for _ in range(N)]
        dfs(i, j, 1, 1)
print(mn)
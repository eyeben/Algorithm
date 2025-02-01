R, C, T = map(int, input().split())
bd = []
for _ in range(R):
    bd.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
vent = []
for i in range(R):
    for j in range(C):
        if bd[i][j] == -1:
            vent.append((j, i))


def moveDust():
    global bd
    dusts = []
    for i in range(R):
        for j in range(C):
            if bd[i][j] and bd[i][j] != -1:
                dusts.append((j, i))

    bd2 = [[0] * C for _ in range(R)]

    for x, y in dusts:
        cnt = 0
        val = bd[y][x]//5
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < C and 0 <= ny <R and (nx,ny) not in vent:
                cnt += 1
                bd2[ny][nx] += val
        bd2[y][x] += bd[y][x] - cnt * val

    for x, y in vent:
        bd2[y][x] = -1

    bd = bd2


def filterDust():
    global bd
    x, y = vent[0]
    bd[y][x] = 0
    y -= 1
    while y > 0:
        bd[y][x] = bd[y-1][x]
        y -= 1
    while x < C-1:
        bd[y][x] = bd[y][x+1]
        x += 1

    while y < vent[0][1]:
        bd[y][x] = bd[y+1][x]
        y += 1

    while 0 < x:
        bd[y][x] = bd[y][x-1]
        x -= 1

    x, y = vent[1]
    bd[y][x] = 0
    y += 1
    while y < R-1:
        bd[y][x] = bd[y + 1][x]
        y += 1
    while x < C - 1:
        bd[y][x] = bd[y][x + 1]
        x += 1
    while vent[1][1] < y:
        bd[y][x] = bd[y - 1][x]
        y -= 1
    while 0 < x:
        bd[y][x] = bd[y][x - 1]
        x -= 1
    for x, y in vent:
        bd[y][x] = -1


for _ in range(T):
    moveDust()
    filterDust()

ans = 0
for itms in bd:
    ans += sum(itms)

print(ans + 2)
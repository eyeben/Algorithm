def checkForBlank(r,c):
    global R,C
    for i in range(4):
        nr, nc = r+dy[i], c+dx[i]
        if 0<=nr<R and 0<=nc<C and bd[nr][nc] == 0:
            return True
    return False

R,C = map(int, input().split())
r,c,d= map(int, input().split())
bd = []
for i in range(R):
    bd.append(list(map(int, input().split())))

if bd[r][c] == 1:
    print(0)
    exit(0)

dx = [0, 1,0,-1]
dy = [-1,0,1,0]

bd[r][c] = 3
ans = 1

while 1:
    if checkForBlank(r,c):
        for _ in range(4):
            d = (d-1) % 4
            nr,nc = r+dy[d], c+dx[d]
            if 0<=nr<R and 0<=nc<C and bd[nr][nc] == 0:
                bd[nr][nc] = 3
                ans += 1
                r,c= nr, nc
                break

    else:
        nd = (d+2)%4
        nr, nc = r+dy[nd], c+dx[nd]
        if not 0<=nr<R or not 0<=nc<C or bd[nr][nc] == 1:
            break
        r,c = nr,nc

print(ans)
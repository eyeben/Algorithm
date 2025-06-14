N, M, K = map(int,input().split())
dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

# bd에 불똥 표시 (3중 리스트로 받아야 함)
bd = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int,input().split())
    bd[r-1][c-1].append((m,s,d))

# new bd1 K번 만큼 돌리기, new bd2로 불똥 분해 구현
for _ in range(K):
    nbd1 = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for m,s,d in bd[y][x]:
                nx, ny = (x + dx[d]*s) % N, (y + dy[d]*s) % N
                nbd1[ny][nx].append((m,s,d))
    nbd2 = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if len(nbd1[y][x]) >= 2:
                allOdd = True
                allEven = True
                ms = 0
                ss = 0
                for m,s,d in nbd1[y][x]:
                    ms += m
                    ss += s
                    if d % 2:
                        allEven = False
                    else:
                        allOdd = False
                ms //= 5
                ss //= len(nbd1[y][x])
                if ms == 0:
                    continue
                start, end = 1, 9
                if allEven or allOdd:
                    start, end = 0, 8
                for i in range(start, end, 2):
                    nbd2[y][x].append((ms, ss, i))
            else:
                nbd2[y][x] += nbd1[y][x]
    bd = nbd2


ans = 0
for i in range(N):
    for j in range(N):
        for m, s, d in bd[i][j]:
            ans += m
print(ans)

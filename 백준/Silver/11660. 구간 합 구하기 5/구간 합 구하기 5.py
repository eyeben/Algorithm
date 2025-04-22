N, M = map(int, input().split())
bd = [[0] * (N+1)]
for _ in range(N):
    bd.append([0] + list(map(int, input().split())))

nu = [[0] *(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        nu[i][j] = nu[i][j-1] + bd[i][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        nu[i][j] += nu[i-1][j]

ans = []
for _ in range(M):
    a,b,c,d = map(int, input().split())
    a -= 1
    b -= 1
    ans.append(nu[c][d] - nu[a][d] - nu[c][b] + nu[a][b])

for itm in ans:
    print(itm)

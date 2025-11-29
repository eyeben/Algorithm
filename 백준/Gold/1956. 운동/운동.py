V, E = map(int, input().split())
BIG = int(1e9)
dists = [[BIG] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dists[a][b] = c

for k in range(V + 1):
    for i in range(V + 1):
        for j in range(V + 1):
            dists[i][j] = min(dists[i][k] + dists[k][j], dists[i][j])

ans = BIG

for i in range(1, V + 1):
    for j in range(1, V + 1):
        if dists[j][i] != BIG and dists[i][j] != BIG:
            ans = min(ans, dists[j][i] + dists[i][j])
print(ans if ans != BIG else -1)
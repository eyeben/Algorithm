N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li2 = []

for i in range(N - 1):
    for j in range(i + 1,N):
        li2.append((li[i][j], i, j))

li2.sort()


parent = [i for i in range(N)]
def get_parent(n):
    if parent[n] != n:
        parent[n] = get_parent(parent[n])
    return parent[n]


def union(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[a] = parent[b]
    elif b < a:
        parent[b] = parent[a]
ans = 0
for d, a, b in li2:
    if get_parent(a) != get_parent(b):
        ans += d
        union(a, b)
print(ans)
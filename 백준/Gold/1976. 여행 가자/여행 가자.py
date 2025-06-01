N = int(input())
M = int(input())

bd = []
for _ in range(N):
    bd.append(list(map(int, input().split())))

plan = list(map(int,input().split()))

parents = [i for i in range(N)]


def findParent(n):
    if parents[n] != n:
        parents[n] = findParent(parents[n])
    return parents[n]

def union(a,b):
    a = findParent(a)
    b = findParent(b)

    if a < b:
        parents[a] = b
    elif b < a:
        parents[b] = a


for i in range(N-1):
    for j in range(i+1, N):
        if bd[i][j]:
            union(i, j)
sett = set()
for num in plan:
    sett.add(findParent(num - 1))
if len(sett) > 1:
    print("NO")
else:
    print("YES")

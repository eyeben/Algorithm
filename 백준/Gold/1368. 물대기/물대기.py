N = int(input())
BIG = 1e9
ans1 = BIG
li = []
tmp = [0]
for _ in range(N):
    tmp.append(int(input()))
li.append(tmp)
for _ in range(N):
    li.append([0] + list(map(int,input().split())))

parents = [i for i in range(N+1)]
def findParent(n):
    if n == parents[n]:
        return n
    parents[n] = findParent(parents[n])
    return parents[n]

def union(a,b):
    a = findParent(a)
    b = findParent(b)

    if a<b:
        parents[b] = a
    elif a>b:
        parents[a] = b

edges = []
for i in range(N):
    for j in range(i+1,N+1):
        edges.append((j,i,li[i][j]))
edges.sort(key = lambda x:x[2])

ans = 0
for x,y,dist in edges:
    if findParent(x) != findParent(y):
        union(x,y)
        ans += dist

print(ans)
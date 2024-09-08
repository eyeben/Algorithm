import math

N = int(input())
li1 = []
for _ in range(N):
    a, b = map(float, input().split())
    li1.append((a,b))

li2 = [[0]*N for _ in range(N)]

for i in range(N-1):
    for j in  range(i+1, N):
        li2[i][j] = math.sqrt((li1[i][0] - li1[j][0])**2 + (li1[i][1] - li1[j][1])**2)

edges = []
for i in range(N-1):
    for j in range(i+1, N):
        edges.append((i,j,li2[i][j]))
edges.sort(key = lambda x:x[2])

parents = [i for i in range(N)]

def findParent(n):
    if parents[n] == n:
        return n
    parents[n] = findParent(parents[n])
    return parents[n]

def union(a,b):
    a= findParent(a)
    b = findParent(b)

    if a<b:
        parents[b] = a
    elif a>b:
        parents[a] = b


total = 0

for x,y,dist in edges:
    if findParent(x) != findParent(y):
        union(x,y)
        total += dist

print(round(total,2))
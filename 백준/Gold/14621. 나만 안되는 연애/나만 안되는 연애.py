N, M = map(int, input().split())

gender = ['W']
gender += input().split()

tmp = []
for _ in range(M):
    tmp.append((map(int,input().split())))

edges = []

for a,b,dist in tmp:
    if gender[a] != gender[b]:
        edges.append((a,b,dist))

edges.sort(key = lambda x:x[2])
parents = [i for i in range(N+1)]

def findParent(n):
    if parents[n] == n:
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

ans = 0
for a,b,dist in edges:
    if findParent(a) != findParent(b):
        union(a,b)
        ans += dist
        
tmp = findParent(1)
for i in range(1,N+1):
    if tmp != findParent(i):
        ans = -1
        break
print(ans)
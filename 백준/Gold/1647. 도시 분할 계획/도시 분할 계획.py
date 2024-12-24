import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []

for _ in range(M):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    li.append((c,a,b))

parents = [i for i in range(N)]
def unionFind(n):
    if parents[n] != n:
        parents[n] = unionFind(parents[n])
    return parents[n]

def union(n1,n2):
    n1 = unionFind(n1)
    n2 = unionFind(n2)
    if n1 < n2:
        parents[n1] = parents[n2]
    elif n2 < n1:
        parents[n2] = parents[n1]

anss = []
li.sort()
for c,a,b in li:
    if unionFind(a) == unionFind(b):
        continue
    union(a,b)
    anss.append(c)
    if len(anss) == N-1:
        break

print(sum(anss) - max(anss))
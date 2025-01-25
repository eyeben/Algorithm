G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

def findParent(n):
    if parent[n] != n:
        parent[n] = findParent(parent[n])
    return parent[n]

def union(a, b):
    a = findParent(a)
    b = findParent(b)
    if a<b:
        parent[b] = a
    elif a>b:
        parent[a] = b


for i in range(P):
    n = int(input())
    k = findParent(n)
    if k == 0:
        print(i)
        exit()
    union(k, k-1)
print(P)
import sys
input = sys.stdin.readline

def findParent(n):
    if parent[n] != n:
        parent[n] = findParent(parent[n])
    return parent[n]


def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[a] = b
        cntDict[a] = cntDict[b] = cntDict[a] + cntDict[b]
    elif a > b:
        parent[b] = a
        cntDict[a] = cntDict[b] = cntDict[a] + cntDict[b]


for i in range(int(input())):
    N = int(input())
    parent = dict()
    cntDict = dict()
    for _ in range(N):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            cntDict[a] = 1
        if b not in parent:
            parent[b] = b
            cntDict[b] = 1
        union(a, b)

        print(cntDict[findParent(a)])

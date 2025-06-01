import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    parents = dict()

    N = int(input())
    for _ in range(N-1):
        a,b = map(int,input().split())
        parents[b] = a

    A,B = map(int,input().split())
    route = set()
    node = A
    while True:
        route.add(node)
        if node not in parents:
            break
        node = parents[node]
    
    ans = -1
    node = B

    while True:
        if node in route:
            print(node)
            break
        if node not in parents:
            break
        node = parents[node]

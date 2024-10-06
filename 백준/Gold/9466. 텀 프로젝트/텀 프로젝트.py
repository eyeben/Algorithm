import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    li = [0] + list(map(int, input().split()))

    isCycle = [-1]*(N+1)

    for i in range(1, N+1):
        if not isCycle[i] == -1:
            continue

        node = i
        visits = defaultdict(int)

        while visits[node] <= 2:
            visits[node] += 1
            node = li[node]
            if not(isCycle[node] == -1):
                break

        for k in visits.keys():
            if visits[k] == 1:
                isCycle[k] = 0
            else:
                isCycle[k] = 1

    print(isCycle.count(0))
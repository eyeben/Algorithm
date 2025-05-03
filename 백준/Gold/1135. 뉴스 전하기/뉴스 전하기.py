from collections import deque

N = int(input())
li = list(map(int, input().split()))


li2 = [[]for _ in range(N)]
for i in range(1, N):
    li2[li[i]].append(i)

def dfs(n):
    if not li2[n]:
        return 0

    tmpList = []
    for itm in li2[n]:
        tmpList.append(dfs(itm))

    tmpList.sort(reverse=True)
    return max([tmpList[i]+i for i in range(len(tmpList))]) + 1
print(dfs(0))

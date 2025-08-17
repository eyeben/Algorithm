from collections import deque
N , M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(M)]

indegree = [0] * (N+1)
arms = [[] for _ in range(N+1)]
for itm in li:
    for idx in range(1, len(itm) - 1):
        arms[itm[idx]].append(itm[idx+1])
        indegree[itm[idx+1]] += 1
ans = []
dq = deque()
for i in range(1, N + 1):
    if not indegree[i]:
        dq.append(i)

while dq:
    n = dq.popleft()
    ans.append(n)
    for itm in arms[n]:
        indegree[itm] -= 1
        if indegree[itm] == 0:
            dq.append(itm)
if len(ans) != N:
    ans = [0]
for itm in ans:
    print(itm)
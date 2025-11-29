from collections import deque
N = int(input())
M = int(input())
li = [list(map(int, input().split())) for _ in range(M)]
smaller = [[] for _ in range(N+1)]
bigger = [[] for _ in range(N+1)]

for a, b in li:
    smaller[a].append(b)
    bigger[b].append(a)


ans = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    visited[i] = True
    dq = deque([i])
    while dq:
        n = dq.popleft()
        for itm in smaller[n]:
            if not visited[itm]:
                visited[itm] = True
                dq.append(itm)

    dq = deque([i])
    while dq:
        n = dq.popleft()
        for itm in bigger[n]:
            if not visited[itm]:
                visited[itm] = True
                dq.append(itm)
    ans.append(str(N - sum(visited)))

print('\n'.join(ans))

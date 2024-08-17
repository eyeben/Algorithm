from collections import deque

N, M = map(int, input().split())

li = [[] for _ in range(N + 1)]
weights = set()
for _ in range(M):
    a, b, c = map(int, input().split())
    li[a].append((b, c))
    li[b].append((a, c))
    weights.add(c)
S, E = map(int, input().split())


def bfs(weightTest):
    visited = [False] * (N + 1)
    dq = deque()
    dq.append(S)
    visited[S] = True

    while dq:
        node = dq.popleft()
        for nextNode, weight in li[node]:
            if not visited[nextNode] and weight >= weightTest:
                dq.append(nextNode)
                visited[nextNode] = True

    return visited[E]


weights = list(weights)
weights.sort()
left = 0
right = len(weights) - 1
ans = 0

while left <= right:
    mid = (left + right) // 2
    weightTest = weights[mid]

    if bfs(weightTest):
        ans = weightTest
        left = mid + 1
    else:
        right = mid - 1

print(ans)
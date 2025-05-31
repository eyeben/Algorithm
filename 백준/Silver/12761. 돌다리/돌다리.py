import heapq
A, B, N, M = map(int,input().split())
dol = [100_001] * 100_001
dol[N] = 0
hq = [(0, N)]
while hq:
    dist, n = heapq.heappop(hq)
    for i in (-1, 1, -A, A, -B, B):
        if 0 <= n + i <= 100_000 and (dist + 1 < dol[n + i]):
            dol[n + i] = dist + 1
            heapq.heappush(hq, (dol[n + i], n + i))

    for i in (A, B):
        if 0 <= n * i <= 100_000 and dist + 1 < dol[n * i]:
            dol[n * i] = dist + 1
            heapq.heappush(hq, (dol[n * i], n * i))

print(dol[M])
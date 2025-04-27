import heapq
def solution(n, works):
    hq = [-itm for itm in works]
    heapq.heapify(hq)
    for _ in range(n):
        heapq.heappush(hq, (heapq.heappop(hq) + 1))
    if hq[0] >= 0:
        return 0
    else:
        ans = 0
        for itm in hq:
            ans += itm**2
        return ans
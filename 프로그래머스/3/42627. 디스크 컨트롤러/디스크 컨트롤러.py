from collections import deque
import heapq
def solution(jobs):
    jobs.sort()
    N = len(jobs)
    hq = []
    clock = 0
    jobs = deque(jobs)
    done = []
    while jobs or hq:
        while jobs and jobs[0][0] <= clock:
            a,b = jobs.popleft()
            heapq.heappush(hq, (b, a))
        if hq:
            b, a = heapq.heappop(hq)
            clock += b
            done.append(clock - a)
        else:
            clock += 1
            
    return (sum(done)//N)
    
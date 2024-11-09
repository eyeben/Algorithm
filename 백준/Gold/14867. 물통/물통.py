import sys
from collections import deque
input = sys.stdin.readline

A,B,C,D = map(int, input().split())

dp = dict()

def funcA(a,b):
    if a + b <= B:
        b += a
        a = 0
    else:
        a = a - (B-b)
        b = B
    return [a,b]


def funcB(a,b):
    if a + b <= A:
        a += b
        b = 0
    else:
        b = b- (A-a)
        a = A
    return [a, b]




dp[(0,0)] = 0
dq = deque()

dq.append((0, 0, 0))
ans = -1
while dq:
    l, r, dist = dq.popleft()

    t1, t2 = funcA(l, r)
    if (t1, t2) not in dp:
        dp[(t1, t2)] = dist + 1
        dq.append((t1, t2, dist + 1))

    t1, t2 = funcB(l, r)
    if (t1, t2) not in dp:
        dp[(t1, t2)] = dist + 1
        dq.append((t1, t2, dist + 1))

    t1, t2 = A, r
    if (t1, t2) not in dp:
        dp[(t1, t2)] = dist + 1
        dq.append((t1, t2, dist + 1))

    t1, t2 = l, B
    if (t1, t2) not in dp:
        dp[(t1, t2)] = dist + 1
        dq.append((t1, t2, dist + 1))

    t1, t2 = 0, r
    if (t1, t2) not in dp:
        dp[(t1, t2)] = dist + 1
        dq.append((t1, t2, dist + 1))

    t1, t2 = l, 0
    if (t1, t2) not in dp:
        dp[(t1, t2)] = dist + 1
        dq.append((t1, t2, dist + 1))

    if (C, D) in dp:
        ans = dp[(C, D)]
        break
print(ans)
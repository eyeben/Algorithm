import copy
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

original = []
for _ in range(N):
    original.append(list(map(int,input().split())))

def makeMove(dir,li):
    # up
    if dir == 0:
        for i in range(N):
            dq = deque()
            for j in range(N):
                if li[j][i]:
                    dq.append(li[j][i])
            if not dq:
                continue
            left = [dq.popleft()]
            while dq:
                if left[-1] == dq[0]:
                    left[-1] *= 2
                    dq.popleft()
                    if dq:
                        left.append(dq.popleft())
                else:
                    left.append(dq.popleft())
            for j in range(N):
                li[j][i] = 0
            for j in range(len(left)):
                li[j][i]= left[j]
    # down
    elif dir == 2:
        for i in range(N):
            dq = deque()
            for j in range(N):
                if li[j][i]:
                    dq.append(li[j][i])
            if not dq:
                continue
            right = deque()
            right.appendleft(dq.pop())
            while dq:
                if right[0] == dq[-1]:
                    right[0] *= 2
                    dq.pop()
                    if dq:
                        right.appendleft(dq.pop())
                else:
                    right.appendleft(dq.pop())
            for j in range(N):
                li[j][i] = 0
            for j in range(len(right)):
                li[N - len(right) + j][i] = right[j]

    # right
    elif dir == 1:
        for i in range(N):
            dq = deque()
            for j in range(N):
                if li[i][j]:
                    dq.append(li[i][j])
            if not dq:
                continue
            right = deque()
            right.appendleft(dq.pop())
            while dq:
                if right[0] == dq[-1]:
                    right[0] *= 2
                    dq.pop()
                    if dq:
                        right.appendleft(dq.pop())
                else:
                    right.appendleft(dq.pop())
            for j in range(N):
                li[i][j] = 0
            for j in range(len(right)):
                li[i][N-len(right)+j]= right[j]



    # left
    elif dir == 3:
        for i in range(N):
            dq = deque()
            for j in range(N):
                if li[i][j]:
                    dq.append(li[i][j])
            if not dq:
                continue
            left = [dq.popleft()]
            while dq:
                if left[-1] == dq[0]:
                    left[-1] *= 2
                    dq.popleft()
                    if dq:
                        left.append(dq.popleft())
                else:
                    left.append(dq.popleft())
            for j in range(N):
                li[i][j] = 0
            for j in range(len(left)):
                li[i][j]= left[j]
    return li

li = copy.deepcopy(original)

mx = 0
def dfs(li, depth):
    global mx
    if depth == 5:
        total = 0
        for itms in li:
            total = max(max(itms),total)
        mx = max(total, mx)
        return
    for i in range(4):
        dfs(makeMove(i, copy.deepcopy(li)), depth + 1)

dfs(copy.deepcopy(original), 0)

print(mx)






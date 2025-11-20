from collections import deque
def solution(ingredient):
    left = []
    right = deque(ingredient)
    cnt = 0
    while right:
        if right[0] == 1 and len(left) >=3 and left[-1] == 3 and left[-2] == 2 and left[-3] == 1:
            left.pop()
            left.pop()
            left.pop()
            right.popleft()
            cnt += 1
        else:
            left.append(right.popleft())
    
    return cnt

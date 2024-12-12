from collections import deque
def solution(number, k):
    right = deque(list(map(int, list(number))))
    right.append(10)
    left = []
    for _ in range(k):
        if not left:
            left.append(right.popleft())
        while left[-1] >= right[0]:
            left.append(right.popleft())
        left.pop(-1)
                
    ans = ''.join(list(map(str, left + list(right)[:-1])))
    return ans
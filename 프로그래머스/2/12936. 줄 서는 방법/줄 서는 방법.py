def solution(n, k):
    from math import factorial
    nums = list(range(1, n + 1))
    k -= 1  # 0-indexed
    answer = []
    
    for i in range(n, 0, -1):
        f = factorial(i - 1)
        idx = k // f
        answer.append(nums.pop(idx))
        k %= f
    
    return answer

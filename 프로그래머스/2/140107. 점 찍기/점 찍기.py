def solution(k, d):
    ans = 0
    n = d // k
    for i in range(0, d + 1, k):
        while i**2 + (n*k)**2 > d*d:
            n -= 1
        ans += 1 + n
    return ans
    
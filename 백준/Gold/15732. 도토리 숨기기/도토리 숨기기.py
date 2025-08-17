N, K, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(K)]


def check(n):
    cnt = D
    for a, b, c in li:
        cnt -= ((min(b,n) - a) // c + 1) if a <= n else 0
    return cnt


left = 1
right = N
ans = N
while left <= right:
    mid = (left + right) // 2
    if check(mid) <= 0:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
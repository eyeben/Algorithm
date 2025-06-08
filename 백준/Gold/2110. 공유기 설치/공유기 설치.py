N,C = map(int, input().split())
li = [int(input()) for _ in range(N)]
li.sort()
left = 1
right = 1_000_000_000
ans = 1

def check(dist):
    cnt = 0
    nowAt = li[0]
    for i in range(1, N):
        if li[i] - nowAt >= dist:
            cnt += 1
            nowAt = li[i]
    return cnt >= C - 1



while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)
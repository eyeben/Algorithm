N, M = map(int, input().split())
Ts = []
for _ in range(N):
    Ts.append(int(input()))


def check(val):
    cnt = 0
    for itm in Ts:
        cnt += val//itm

    return M <= cnt


left, right = 0, min(Ts)*M
ans = 0

while left <= right:
    mid = (left+right) // 2
    if check(mid):
        ans = mid
        right = mid -1
    else:
        left = mid + 1


print(ans)
N = int(input())
li = list(map(int, input().split()))
M = int(input())
left, right = 0, max(li)
ans = 0


def check(n):
    total = 0
    for itm in li:
        total += min(itm, n)
    return total <= M


while left <= right:
    mid = (left+right) // 2
    if check(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)

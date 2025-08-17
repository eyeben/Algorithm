N = int(input())
M = int(input())
li = list(map(int, input().split()))
li.sort()
ans = 0
left = 0
right = N - 1
while left < right:
    if li[left] + li[right] > M:
        right -= 1
    elif li[left] + li[right] < M:
        left += 1
    else:
        ans += 1
        left += 1
        right -= 1
print(ans)
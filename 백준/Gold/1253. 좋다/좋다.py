import sys
input = sys.stdin.readline
N = int(input())

li = list(map(int,input().split()))
li.sort()
# N = 1
# N = 2
if N<=2:
    print(0)
    exit()

able = [False]*N

# 왼+왼 = 오
for i in range(2, N):
    left, right = 0, i-1
    while left<right:
        if li[left] + li[right] < li[i]:
            left += 1
        elif li[i] < li[left] + li[right]:
            right -= 1
        else:
            able[i] = True
            break
# 왼 = 오+오

for i in range(N-2):
    left, right = i+1, N-1
    while left<right:
        if li[left] + li[right] < li[i]:
            left += 1
        elif li[i] < li[left] + li[right]:
            right -= 1
        else:
            able[i] = True
            break


# 가 = 왼 + 오
for i in range(1, N-1):
    left, right = 0, N-1
    while left < i < right:
        if li[left] + li[right] < li[i]:
            left += 1
        elif li[i] < li[left] + li[right]:
            right -= 1
        else:
            able[i] = True
            break
print(sum(able))
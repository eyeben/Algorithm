import sys
import heapq
input = sys.stdin.readline
N = int(input())
li = list(map(int,input().split()))
left = []
right = []
for itm in li:
    if itm >= 0:
        right.append(itm)
    else:
        left.append(itm)

left.sort(reverse=True)
right.sort()
ans1, ans2 = 0, 0
mn = int(1e10)
if len(left) >= 2:
    if abs(left[0] + left[1]) < mn:
        mn = abs(left[0] + left[1])
        ans1,ans2 = left[1], left[0]

if len(right) >= 2:
    if abs(right[0] + right[1]) < mn:
        mn = abs(right[0] + right[1])
        ans1,ans2 = right[0], right[1]

while left and right:
    if abs(left[-1] + right[-1]) < mn:
        ans1,ans2 = left[-1], right[-1]
        mn = abs(left[-1] + right[-1])

    if 0 < left[-1] + right[-1]:
        right.pop()
    elif left[-1] + right[-1] < 0:
        left.pop()
    else:
        break

print(ans1, ans2)
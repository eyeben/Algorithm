N = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
M = int(input())

def check(mid):
    total = 0
    for itm in li:
        total += min(itm, mid)
        if total>M:
            return False
    return True

ans = 0
left = 0
right = max(li)
while left<= right:
    mid = (left+right)//2
    if check(mid):
        ans = mid
        left = mid+1
    else:
        right = mid-1

print(ans)
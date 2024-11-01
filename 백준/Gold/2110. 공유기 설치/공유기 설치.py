import sys

input = sys.stdin.readline


def check(piv):
    cnt = 1
    prev = 0
    cur = 1
    while cur<N:
        if li[cur] - li[prev] >= piv:
            cnt += 1
            if cnt == C:
                return True
            prev = cur
        cur += 1
        
    return False

N, C = map(int,input().split())
li = [int(input()) for _ in range(N)]

li.sort()
right = li[-1] - li[0]
left = 0
ans = -1
while left <= right:
    piv = (left + right)//2
    if check(piv):
        left = piv + 1
        ans = piv
    else:
        right = piv -1

print(ans)
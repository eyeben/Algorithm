import sys
input = sys.stdin.readline
N = int(input())

li = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()
elif N == 2:
    print(1)
    exit()

mx = 0
for i in range(N):
    height = li[i]
    left = []
    right = []
    for l in range(i):
        left.append((height - li[l])/(i-l))
    for r in range(i+1,N):
        right.append((height - li[r]) / (i - r))

    cnt = 0
    if left:
        cnt+=1
        piv = left[-1]
        for j in range(len(left)-1,-1,-1):
            if piv > left[j]:
                cnt += 1
                piv = left[j]

    if right:
        cnt+=1
        piv = right[0]
        for j in range(len(right)):
            if piv < right[j]:
                cnt += 1
                piv = right[j]

    mx = max(mx, cnt)

print(mx)
N = int(input())
li = list(map(int, input().split()))
cnt = int(input())
start = 0
while cnt and start < N:
    mx = max(li[start:start+cnt+1])
    idx = li.index(mx)
    li = li[:start] + [mx] + li[start:idx] + li[idx+1:]
    cnt -= idx - start
    start += 1
print(*li)

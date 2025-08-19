N = int(input())
li = [int(input()) for _ in range(N)]

ans = []
stk = []
idx = 0
num = 1
for idx in range(N):
    while num <= li[idx]:
        stk.append(num)
        ans.append('+')
        num += 1
    if stk[-1] != li[idx]:
        print("NO")
        exit(0)
    ans.append('-')
    stk.pop()
for itm in ans:
    print(itm)
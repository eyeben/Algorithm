from collections import defaultdict
N = int(input())
li = list(map(int, input().split()))
BIGGEST = max(li)
nums = [False] * (BIGGEST + 1)
for itm in li:
    nums[itm] = True
score = defaultdict(int)

for i in range(N):
    num = li[i]
    while num <= BIGGEST:
        if nums[num]:
            score[li[i]] += 1
            score[num] -= 1
        num += li[i]

anss = [0]*N

for i in range(N):
    anss[i] = score[li[i]]
print(*anss)
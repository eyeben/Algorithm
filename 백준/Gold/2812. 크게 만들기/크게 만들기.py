import heapq
from collections import defaultdict

N, K = map(int, input().split())
li = list(map(int, list(input())))
dic = defaultdict(list)

for i in range(K):
    dic[li[i]].append(i)

for i in range(10):
    heapq.heapify(dic[i])

ans1 = []
head = 0
for i in range(K, N):
    heapq.heappush(dic[li[i]], i)
    for j in range(9, -1, -1):
        if dic[j]:
            idx = heapq.heappop(dic[j])
            ans1.append((j, idx))
            for k in range(head, idx):
                heapq.heappop(dic[li[k]])
            head = idx + 1
            break
ans1.sort(key=lambda x: x[1])
ans = [str(itm[0]) for itm in ans1]
print(''.join(ans))

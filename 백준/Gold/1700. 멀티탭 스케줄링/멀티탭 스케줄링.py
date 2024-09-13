from collections import defaultdict
from collections import deque
N,K =map(int,input().split())

li = list(map(int,input().split()))

mapper = defaultdict(deque)
# 물건별 인덱스 기록
for i in range(K):
    mapper[li[i]].append(i)
# 사전작업: 꽂아놓고 사전에서 삭제
multiTab = set()
start =0
while start<K:
    if len(multiTab) == N:
        break
    multiTab.add(li[start])
    mapper[li[start]].popleft()
    start+=1

multiTab = list(multiTab)
ans = 0

for i in range(start,K):
    num = li[i]
    if num not in multiTab:
        mx = 0
        multiTabIdx = 0
        for j in range(len(multiTab)):
            if not mapper[multiTab[j]]:
                multiTabIdx = j
                break
            if mx < mapper[multiTab[j]][0]:
                mx = mapper[multiTab[j]][0]
                multiTabIdx = j
        ans+=1
        multiTab[multiTabIdx] = num

    mapper[num].popleft()

print(ans)
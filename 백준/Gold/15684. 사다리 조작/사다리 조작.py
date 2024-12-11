from itertools import combinations
N, M, H = map(int, input().split())
li = [[False] * (N-1) for _ in range(H)]
for i in range(M):
    a,b = map(int,input().split())
    li[a-1][b-1] = True


def draw(n):
    nowAt = n
    for i in range(H):
        if nowAt -1 >=0 and li[i][nowAt-1]:
            nowAt -= 1
        elif nowAt +1<N and li[i][nowAt]:
            nowAt += 1
    return nowAt == n
cnt = 0

for i in range(N):
    cnt += draw(i)
if N-cnt > 6:
    print(-1)
    exit()

all = []
for i in range(N-1):
    for j in range(H):
        if not li[j][i]:
            all.append((i,j))
combi = []
for i in range(4):
    combi += list(combinations(all,i))
for itms in combi:

    for x,y in itms:
        li[y][x] = True
    goodFlag = True
    for i in range(N):
        if not draw(i):
            goodFlag = False
            break

    if goodFlag:
        print(len(itms))
        exit()
    for x,y in itms:
        li[y][x] = False
print(-1)
N = int(input())
li = []

for _ in range(N):
    tmp = list(input())
    tmp2 = []
    for itm in tmp:
        if itm == '0':
            tmp2.append(0)
        elif ord('a') <= ord(itm) <= ord('z'):
            tmp2.append(ord(itm)-ord('a')+1)
        else:
            tmp2.append(ord(itm) - ord('A') + 27)

    li.append(tmp2)

li2 = []
ans1 = 0
for i in range(N):
    for j in range(N):
        if(li[i][j]):
            li2.append((li[i][j], i, j))

li2.sort()
parent =  [i for i in range(N)]
def findParent(n):
    if parent[n] != n:
        parent[n] = findParent(parent[n])
    return parent[n]

def union(a,b):
    a = findParent(a)
    b = findParent(b)

    if a < b:
        parent[a] = b
    elif a>b:
        parent[b] = a
cnt = 0
for d,i,j in li2:
    if findParent(i) == findParent(j):
        continue
    union(i,j)
    cnt += 1
    ans1 += d
ans2 = 0
for itm in li:
    ans2 += sum(itm)

ans = ans2 - ans1
if cnt != N-1:
    ans = -1
print(ans)
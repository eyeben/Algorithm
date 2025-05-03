N = int(input())
li = [[0,0,0,0]]+[list(map(int, input().split())) for _ in range(N)]
N += 1
li2 = [set() for _ in range(N)]

for k in range(N):
    a, b, c, d = li[k]
    tmp = []
    for i in range(min(a, c), max(a,c) + 1):
        tmp.append((i, b))
        tmp.append((i, d))
    for i in range(min(b, d), max(b,d) + 1):
        tmp.append((a, i))
        tmp.append((c, i))
    li2[k] = set(tmp)

touches = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        for itm in li2[i]:
            if itm in li2[j]:
                if i == 3 and j ==4:
                    print(itm, li2[j])
                touches[i].append(j)
                touches[j].append(i)
                break

parents = [i for i in range(N)]
def findParent(n):
    if parents[n] != n:
        parents[n] = findParent(parents[n])
    return parents[n]

def unify(a,b):
    a = findParent(a)
    b = findParent(b)
    if a<b:
        parents[b] = a
    elif b<a:
        parents[a] = b

for i in range(N):
    for itm in touches[i]:
        unify(i,itm)

anss = set()
for itm in parents:
    anss.add(findParent(itm))
print(len(anss)-1)
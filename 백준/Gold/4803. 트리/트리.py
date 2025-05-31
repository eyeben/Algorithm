testNum = 1
while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    dots = []
    for _ in range(M):
        dots.append(list(map(int, input().split())))
    parents = [i for i in range(N+1)]
    isTree = True

    def findParent(n):
        if parents[n] != n:
            parents[n] = findParent(parents[n])
        return parents[n]

    def union(a,b):
        a = findParent(a)
        b = findParent(b)
        if a < b:
            parents[a] = b
        elif b < a:
            parents[b] = a

    badTrees = set()
    for a, b in dots:
        if findParent(a) == findParent(b):
            badTrees.add(findParent(a))
            continue
        union(a, b)
    trees = set()
    for i in range(1, N+1):
        trees.add(findParent(i))
    realBadTrees = set()
    for itm in badTrees:
        realBadTrees.add(findParent(itm))
    cnt = len(trees) - len(realBadTrees)
    print("Case " + str(testNum) + ":", end = ' ')
    if cnt == 0:
        print("No trees.")
    elif cnt == 1:
        print("There is one tree.")
    else:
        print("A forest of", cnt, "trees.")

    testNum += 1


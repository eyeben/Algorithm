li = []
for _ in range(9):
    li.append(list(map(int, input().split())))


def getSquareValues(x, y):
    tmp = []
    nx, ny = x // 3, y // 3
    for i in range(3 * nx, 3 * nx + 3):
        for j in range(3 * ny, 3 * ny + 3):
            tmp.append(li[j][i])
    return tmp


def getYChookValues(x, y):
    tmp = []
    for i in range(9):
        tmp.append(li[i][x])
    return tmp


def getXChookValues(x, y):
    tmp = []
    for i in range(9):
        tmp.append(li[y][i])
    return tmp


def isJoongBock(tmpList):
    nums = [0] * 10
    for itm in tmpList:
        nums[itm] += 1
    for i in range(1, 10):
        if nums[i] > 1:
            return True
    return False


dic = dict()

for i in range(9):
    for j in range(9):
        if li[i][j] != 0:
            continue

        tmp = [1] * 10
        for num in getSquareValues(j, i):
            tmp[num] = 0
        for num in getXChookValues(j, i):
            tmp[num] = 0
        for num in getYChookValues(j, i):
            tmp[num] = 0

        if (sum(tmp[1:]) == 1):
            li[i][j] = tmp[1:].index(1) + 1
            continue

        dic[(j, i)] = []

        for k in range(1, 10):
            if tmp[k]:
                dic[(j, i)].append(k)

dicKeys = list(dic.keys())
dicKeys.sort(key = lambda x: x[0]//3)
dicKeys.sort(key = lambda x: x[1]//3)
dicValues = [dic[k] for k in dicKeys]


def backTrack(idx):
    if idx == len(dicKeys):
        for itms in li:
            print(' '.join(list(map(str, itms))))
        exit(0)

    x, y = dicKeys[idx][0], dicKeys[idx][1]
    for itm in dicValues[idx]:
        li[y][x] = itm
        if isJoongBock(getXChookValues(x, y)) or isJoongBock(getYChookValues(x, y)) or isJoongBock(getSquareValues(x, y)):
            li[y][x] = 0
            continue
        backTrack(idx + 1)
        li[y][x] = 0


backTrack(0)

print(li[100][100])
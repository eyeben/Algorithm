li = []
for _ in range(9):
    li.append(list(map(int, input().split())))


# 같은 사각형 안의 값을 리스트로 반환
def getSquareValues(x, y):
    tmp = []
    nx, ny = x // 3, y // 3
    for i in range(3 * nx, 3 * nx + 3):
        for j in range(3 * ny, 3 * ny + 3):
            tmp.append(li[j][i])
    return tmp

# 같은 y축 위의 값을 리스트로 반환
def getYChookValues(x, y):
    tmp = []
    for i in range(9):
        tmp.append(li[i][x])
    return tmp

# 같은 x축 위의 값을 리스트로 반환
def getXChookValues(x, y):
    tmp = []
    for i in range(9):
        tmp.append(li[y][i])
    return tmp

# 입력 받은 리스트 안에 중복 되는 값이 있는지 체크
def isJoongBock(tmpList):
    nums = [0] * 10
    for itm in tmpList:
        nums[itm] += 1
    for i in range(1, 10):
        if nums[i] > 1:
            return True
    return False

# 빈칸을 찾고 사전에 빈칸 마다 들어올 수 있는 값 후보들을 저장
dic = dict()
# 빈칸 찾기
for i in range(9):
    for j in range(9):
        if li[i][j] != 0:
            continue

        # 후보 찾기
        tmp = [1] * 10
        for num in getSquareValues(j, i):
            tmp[num] = 0
        for num in getXChookValues(j, i):
            tmp[num] = 0
        for num in getYChookValues(j, i):
            tmp[num] = 0
        # 후보가 하나면 걍 넣어줌
        if (sum(tmp[1:]) == 1):
            li[i][j] = tmp[1:].index(1) + 1
            continue

        # 후보 저장
        dic[(j, i)] = []
        for k in range(1, 10):
            if tmp[k]:
                dic[(j, i)].append(k)

dicKeys = list(dic.keys())
# 최적화: 같은 정사각형 애들 먼저, 후보 적은 칸 먼저
dicKeys.sort(key = lambda x: len(dic[x]))
dicKeys.sort(key = lambda x: x[0]//3)
dicKeys.sort(key = lambda x: x[1]//3)

dicValues = [dic[k] for k in dicKeys]

# 백트랙킹을 수행하나 끝까지 도달하면 출력 후 프로그램 종료
def backTrack(idx):
    if idx == len(dicKeys):
        for itms in li:
            print(' '.join(list(map(str, itms))))
        exit(0)

    x, y = dicKeys[idx][0], dicKeys[idx][1]
    for itm in dicValues[idx]:
        li[y][x] = itm
        # 중복 체크 후 없으면 다음 후보
        if isJoongBock(getXChookValues(x, y)) or isJoongBock(getYChookValues(x, y)) or isJoongBock(getSquareValues(x, y)):
            continue
        backTrack(idx + 1)
    li[y][x] = 0


backTrack(0)

print(li[100][100])
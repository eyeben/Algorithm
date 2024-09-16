import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

li = []
bd = [[0] * M for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    tmp = []
    for _ in range(a):
        tmp.append(list(map(int, input().split())))
    li.append((tmp))


def rotate(arr):
    m = len(arr[0])
    n = len(arr)
    new_arr = [[0] * n for _ in range(m)]

    for y in range(n):
        for x in range(m):
            new_arr[x][n - 1 - y] = arr[y][x]
    return new_arr


def check(x, y, arr):
    m = len(arr[0])
    n = len(arr)

    if M < x + m or N < y + n:
        return False

    for i in range(m):
        for j in range(n):
            if arr[j][i] == 1 and bd[y+j][x+i] == 1:
                return False

    return True

def fill(x, y, arr):
    global bd
    m = len(arr[0])
    n = len(arr)
    for i in range(m):
        for j in range(n):
            if arr[j][i] == 1 and bd[j+y][i+x] == 0:
                bd[j+y][i+x] = 1

for arr in li:
    goodflag = False
    for round in range(4):
        for i in range(N):
            for j in range(M):
                if check(j,i,arr):
                    fill(j,i,arr)
                    goodflag = True
                    break
            if goodflag:
                break
        if goodflag:
            break
        arr = rotate(arr)

ans = 0
for itms in bd:
    ans += sum(itms)

print(ans)
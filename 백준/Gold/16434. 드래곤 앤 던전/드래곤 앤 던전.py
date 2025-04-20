N, A = map(int,input().split())
li = []
for _ in range(N):
    li.append(list(map(int,input().split())))

left = 0
right = int(1e50)
ans = 0


def check(num):
    atk = A
    curH = num
    for i in range(N):
        if li[i][0] == 1:
            turnToWin = li[i][2] // atk
            if li[i][2] % atk:
                turnToWin += 1
            if li[i][1] * (turnToWin - 1) >= curH:
                return False
            curH -= li[i][1] * (turnToWin -1)
        else:
            curH = min(num, curH + li[i][2])
            atk += li[i][1]
    return curH > 0


while left <= right:
    mid = (left+right) // 2
    if check(mid):
        ans = mid
        right = mid - 1

    else:
        left = mid + 1

print(ans)
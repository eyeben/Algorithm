N = int(input())

cmds = []
for _ in range(N):
    cmds.append(list(map(int, input().split())))

mark0 = set()

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def dofunc(X,Y,D,L):
    global mark0
    level = 0
    startX = X
    startY = Y
    endX = X+dx[D]
    endY = Y+dy[D]
    sett = set()
    sett.add((X,Y))
    sett.add((endX,endY))
    while level < L:
        tmp = set()
        for x, y in sett:
            tmp.add((endX - (y - endY), endY + (x - endX)))

        endX, endY = endX - (startY - endY), endY + (startX - endX)

        sett.update(tmp)
        level += 1
    mark0.update(sett)



for x,y,d,l in cmds:
    dofunc(x,y,d,l)

ans = 0
for x,y in mark0:
    if (x+1,y) in mark0 and (x,y+1) in mark0 and (x+1,y+1) in mark0:
        ans += 1

print(ans)
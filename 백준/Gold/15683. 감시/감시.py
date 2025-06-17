import copy

N, M = map(int, input().split())

dy = [-1,0,1,0]
dx = [0,1,0,-1]


def color(x, y ,d, board):
    if d == 0:
        while y-1 >= 0:
            if board[y-1][x] == 0:
                board[y-1][x] = "#"
                y -= 1
            elif board[y-1][x] == 6:
                break
            else:
                y -= 1

    elif d == 2:
        while y+1 < N:
            if board[y+1][x] == 0:
                board[y+1][x] = "#"
                y += 1
            elif board[y+1][x] == 6:
                break
            else:
                y += 1

    elif d == 1:
        while x+1 < M:
            if board[y][x+1] == 0:
                board[y][x+1] = '#'
                x += 1
            elif board[y][x+1] == 6:
                break
            else:
                x+=1
    elif d == 3:
        while 0 <= x-1:
            if board[y][x-1] == 0:
                board[y][x-1] = '#'
                x += 1
            elif board[y][x-1] == 6:
                break
            else:
                x-=1

def markVision(board, x,y, num, d):
    if num == 1:
        color(x, y ,d, board)
    elif num == 2:
        color(x, y ,d, board)
        color(x, y ,(d+2) % 4, board)
    elif num == 3:
        color(x, y ,d, board)
        color(x, y ,(d+1) % 4, board)
    elif num == 4:
        color(x, y ,(d+1)%4, board)
        color(x, y ,(d+2)%4, board)
        color(x, y ,(d+3)%4, board)
    elif num == 5:
        color(x, y ,d, board)
        color(x, y ,(d+1)%4, board)
        color(x, y ,(d+2)%4, board)
        color(x, y ,(d+3)%4, board)
def dfs(board):
    global ANS
    if not CCTV:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cnt+=1
        ANS = min(cnt, ANS)
        return
    
    x,y = CCTV.pop()
    num = li[y][x]
    if num == 5:
        nli = copy.deepcopy(board)
        markVision(nli, x,y, num, 0)
        dfs(nli)

    elif num == 2:
        for i in range(2):
            nli = copy.deepcopy(board)
            markVision(nli, x,y, num, i)
            dfs(nli)
            

    else:
        for i in range(4):
            nli = copy.deepcopy(board)
            markVision(nli, x,y, num, i)
            dfs(nli)

    CCTV.append((x,y))



li = []
for i in range(N):
    li.append(list(map(int,input().split())))

CCTV = [] # (x,y)s
for i in range(N):
    for j in range(M):
        if li[i][j] != 0 and li[i][j] != 6:
            CCTV.append((j,i))

ANS = M*N

dfs(li)
print(ANS)
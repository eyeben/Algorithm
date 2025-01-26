import copy
def solution(m, n, board):
    new_arr = [[0]*m for _ in range(n)]
    for y in range(m):
        for x in range(n):
            new_arr[x][m - 1 - y] = board[y][x]
    board = copy.deepcopy(new_arr)

    # print(board)
    def check(x,y):
        if board[y][x] == '.':
            return False
        return board[y][x] == board[y][x+1]== board[y+1][x]== board[y+1][x+1]
    
    
    changeFlag = True
    
    while changeFlag:
        changeFlag = False
        tfBoard = [[False]*m for _ in range(n)]
        for i in range(m-1): # x
            for j in range(n-1): # y
                if check(i, j):
                    changeFlag = True
                    tfBoard[j][i] = tfBoard[j+1][i] = tfBoard[j][i+1] = tfBoard[j+1][i+1] = True
                    
        newBoard = []
        for i in range(n): # y
            tmp = []
            for j in range(m): # x
                if tfBoard[i][j]:
                    continue
                tmp.append(board[i][j])
            tmp += ['.']*(m-len(tmp))
            newBoard.append(tmp)
        board = copy.deepcopy(newBoard)
    # print(board)
    answer = 0
    for itms in board:
        answer += itms.count('.')
    return answer
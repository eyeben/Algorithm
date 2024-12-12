def solution(board, skill):
    board2 = [[0]*(len(board[0])+2) for _ in range(len(board)+2)]
    
    for t, y1,x1, y2, x2, amount in skill:
        y1,y2 = min(y1,y2)+1, max(y1,y2)+1
        x1,x2 = min(x1,x2)+1, max(x1,x2)+1
        if t == 1:
            amount *= -1
        board2[y1][x1] += amount
        board2[y1][x2+1] -= amount
        board2[y2+1][x1] -= amount
        board2[y2+1][x2+1] += amount

    for x in range(1,len(board[0])+1):
        for y in range(1,len(board)+1):
            board2[y][x] += board2[y][x-1]
    
    for x in range(1,len(board[0])+1):
        for y in range(1,len(board)+1):
            board2[y][x] += board2[y-1][x]

    ans = 0
    
    for x in range(0,len(board[0])):
        for y in range(0,len(board)):
            #board[y][x] = board[y][x] + board2[y+1][x+1]
            if board[y][x] + board2[y+1][x+1] > 0:
                ans+=1
                
    return ans
def solution(m, n, puddles):
    li = [[-1] * m for _ in range(n)]
    li[0][0] = 1
    for x,y in puddles:
        li[y-1][x-1] = 0
        
    for i in range(1,m):
        if li[0][i] == -1:
            li[0][i] = li[0][i-1]
    for i in range(1,n):
        if li[i][0] == -1:
            li[i][0] = li[i-1][0]
        
    for y in range(1,n):
        for x in range(1,m):
            if li[y][x] == -1:
                li[y][x] = (li[y-1][x] + li[y][x-1]) % 1_000_000_007

    if li[-1][-1] == -1:
        return 0
    return li[-1][-1]
    
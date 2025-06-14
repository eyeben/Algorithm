def solution(board):
    N, M = len(board), len(board[0])
    nu = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            nu[i+1][j+1] = nu[i+1][j] + nu[i][j+1] - nu[i][j] + board[i][j]

    def check(n):
        for i in range(1 + n, N+1):
            for j in range(1 + n, M+1):
                if nu[i][j] - nu[i][j-1-n] - nu[i-1-n][j] + nu[i-1-n][j-1-n] == (n+1)**2:
                    return True
        return False
    
    start = 0
    end = min(N, M)
    ans = 0
    while start <= end:
        mid = (start + end)//2
        if check(mid):
            ans = (mid + 1)**2
            start = mid + 1
        else:
            end = mid - 1
    return ans
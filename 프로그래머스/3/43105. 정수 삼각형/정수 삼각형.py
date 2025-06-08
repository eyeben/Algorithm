def solution(triangle):
    N = len(triangle)
    anss = [0] * N
    anss[0] = triangle[0][0]
    for i in range(1, N):
        tmp = anss[:]
        tmp[0] = anss[0] + triangle[i][0]
        tmp[i] = anss[i-1] + triangle[i][-1]
        for j in range(1, i):
            tmp[j] = triangle[i][j] + max(anss[j-1], anss[j])
        anss = tmp
        
    return max(anss)
    
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][(j+1)%4],land[i-1][(j+2)%4],land[i-1][(j+3)%4])
    return max(land[-1])
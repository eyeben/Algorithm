def solution(players, m, k):
    ans = 0
    
    li = [[i, 0] for i in players]

    for i in range(24):
        if li[i][0] > li[i][1] * m:
            cnt = li[i][0] // m - li[i][1]
            for j in range(i, min(24, i + k)):
                li[j][1] += cnt
            ans += cnt
    return ans
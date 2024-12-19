N = int(input())//3




def dfs(ans, level):
    if level == 1:
        return ans
    nextAns = []
    H = len(ans)
    L = len(ans[0])
    for i in range(H):
        nextAns.append(' '*(L//2 + 1) + ans[i] + ' '*(L//2 + 1))
    for i in range(H):
        nextAns.append(ans[i]+" "+ans[i])

    return dfs(nextAns, level//2)





ans = ["  *  "," * * ","*****"]

ans2 = dfs(ans, N)

for itms in ans2:
    print(itms)
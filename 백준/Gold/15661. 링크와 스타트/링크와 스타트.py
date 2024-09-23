N = int(input())

li =[]
for _ in range(N):
    li.append(list(map(int, input().split())))
ans = int(1e9)
def dfs(piv,leftList, rightList, leftVal, rightVal):
    global ans
    if piv == N:
        ans = min(ans, abs(rightVal-leftVal))
        return

    dfs(piv+1, leftList+[piv], rightList, leftVal+ sum([li[piv][idx]+li[idx][piv]for idx in leftList]), rightVal)
    dfs(piv + 1, leftList, rightList+[piv], leftVal , rightVal+ sum([li[piv][idx] + li[idx][piv] for idx in rightList]))


dfs(0,[],[],0,0)
print(ans)
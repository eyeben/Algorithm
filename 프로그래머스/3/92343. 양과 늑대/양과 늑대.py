def solution(info, edges):
    ans = 0
    visited = [False]*len(info)
    def dfs(sCnt, wCnt):
        nonlocal ans
        if sCnt <= wCnt:
            return
        ans = max(ans, sCnt)
        for a,b in edges:
            if visited[a] and not visited[b]:
                visited[b] = True
                if info[b]:
                    dfs(sCnt, wCnt+1)
                else:
                    dfs(sCnt+1, wCnt)
                visited[b] = False
    visited[0] = True
    dfs(1,0)
    return ans
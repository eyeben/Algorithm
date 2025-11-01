from collections import deque
def solution(storage, requests):
    N = len(storage) + 2
    M = len(storage[0]) + 2
    ns = [['.']*M] + [['.']+list(itm)+['.'] for itm in storage] + [['.']*M]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def func1(letter):
        cnt = 0
        visited = [[False] * M for _ in range(N)]
        dq = deque([(0,0)])
        visited[0][0] = True
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                nx, ny = x + dx[i] , y + dy[i]
                if not (0 <= nx < M and 0 <= ny < N) or visited[ny][nx]:
                    continue
                if letter == ns[ny][nx]:
                    ns[ny][nx] = '.'
                    visited[ny][nx] = True
                    cnt += 1
                elif '.' == ns[ny][nx]:
                    visited[ny][nx] = True
                    dq.append((nx, ny))
        return cnt
                    
    def func2(letter):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if letter == ns[i][j]:
                    ns[i][j] = '.'
                    cnt += 1
        return cnt

    ans = (M-2) * (N-2)
    for itm in requests:
        if len(itm) == 1:
            ans -= func1(itm)
        else:
            ans -= func2(itm[0])
    return ans
    
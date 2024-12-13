import sys
from collections import deque
input= sys.stdin.readline
T = int(input())


for _ in range(T):
    M,N,K = map(int, input().split())

    bd = [[0]*M for _ in range(N)]

    for _ in range(K):
        a,b = map(int, input().split())
        bd[b][a] = 1

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    def bfs():
        cnt = 0
        visited = [[False]*M for _ in range(N)]
        for i in range(M): #x
            for j in range(N): #y
                if not visited[j][i] and bd[j][i] == 1:
                    cnt += 1

                    dq = deque([(i,j)])
                    visited[j][i] = True
                    while dq:
                        x,y = dq.popleft()
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and bd[ny][nx]:
                                visited[ny][nx] = True
                                dq.append((nx,ny))

        return cnt

    print(bfs())
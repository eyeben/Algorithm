from collections import deque
from time import sleep

N, M = map(int, input().split())
N += 1
li = [list(input()) for _ in range(N-1)]
li.append(['x'] * M)
K = int(input())
cmd = list(map(int, input().split()))

dx = [0,1,0,-1]
dy = [-1,0,1,0]


def dropMinerals():
    cnt = 1
    visited = [[0]*M for _ in range(N)]

    for i in range(M-1,-1,-1):
        for j in range(N-1,-1,-1):
            if li[j][i] == 'x' and not visited[j][i]:
                dq = deque([(i,j)])
                visited[j][i] = cnt
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<=nx<M and 0<=ny<N and li[ny][nx] == 'x' and not visited[ny][nx]:
                            visited[ny][nx] = cnt
                            dq.append((nx,ny))

                cnt += 1


    while True:
        noChange = True
        for k in range(2, cnt):
            gap = True
            for i in range(M):
                for j in range(N-1):
                    if visited[j][i] == k and visited[j+1][i] != k and visited[j+1][i]:
                        gap = False
                        break

            if gap:
                for i in range(M):
                    for j in range(N - 2,-1,-1):
                        if visited[j][i] == k:
                            visited[j+1][i] = k
                            visited[j][i] = 0
                            li[j+1][i] = 'x'
                            li[j][i] = '.'
                noChange = False

        if noChange:
            break




for i in range(K):
    y = N -1 - cmd[i]
    if i % 2 == 0: # 왼쪽
        for j in range(M):
            if li[y][j] == 'x':
                li[y][j] = '.'
                dropMinerals()
                break
    else: # 오른쪽
        for j in range(M-1,-1,-1):
            if li[y][j] == 'x':
                li[y][j] = '.'
                dropMinerals()
                break



for itms in li[:-1]:
    print(''.join(itms))
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    li.append(list(input().strip()))
# B 위치 찾기
isHori = False
bx,by = -1, -1
for i in range(N):
    for j in range(N):
        if li[i][j] == 'B':
            isHori = (j != N-1 and li[i][j+1] == 'B')
            bx, by = j, i
            break
    if bx != -1:
        break
# E 위치 찾기
eHori = False
ex,ey = -1, -1
for i in range(N):
    for j in range(N):
        if li[i][j] == 'E':
            eHori = j != N-1 and li[i][j+1] == 'E'
            ex,ey = j, i
            break
    if ex != -1:
        break

# DP 초기화
horiDp = [[-2]*N for _ in range(N)]
vertDp = [[-2]*N for _ in range(N)]

d = [0,-1,-2]


# 1인 경우 안되는 자리들 표기
for i in range(N):
    for j in range(N):
        if li[i][j] == '1':
            for k in range(3):
                nx,ny = j, i + d[k]
                if 0<=nx<N and 0<=ny<N:
                    vertDp[ny][nx] = -1
                nx, ny = j + d[k], i
                if 0 <= nx < N and 0 <= ny < N:
                    horiDp[ny][nx] = -1

# 끝에 안되는 위치들 표기
for i in range(N-2,N):
    for j in range(N):
        vertDp[i][j] = -1
        horiDp[j][i] = -1


if isHori:
    horiDp[by][bx] = 0
else:
    vertDp[by][bx] = 0

dq = deque()
dq.append((bx,by,isHori,0))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
while dq:
    x,y,isHori,dist = dq.popleft()
    # -
    if isHori:
        # 상하좌우
        for i in range(4):
            nx, ny = x +dx[i], y + dy[i]
            if not(0<=nx<N and 0<=ny<N):
                continue
            if horiDp[ny][nx] == -2:
                horiDp[ny][nx] = dist + 1
                dq.append((nx,ny,True,dist+1))
        # 돌리기
        nx, ny = x + 1, y - 1
        if 0 <= nx < N and 0 <= ny < N and vertDp[ny][nx] == -2:
            if y+1 < N and horiDp[y+1][x] != -1 and 0 <= y-1 and horiDp[y-1][x] != -1:
                vertDp[ny][nx] = dist + 1
                dq.append((nx, ny, False, dist + 1))
    # |
    else:
        # 상하좌우
        for i in range(4):
            nx, ny = x +dx[i], y + dy[i]
            if not(0<=nx<N and 0<=ny<N):
                continue
            if vertDp[ny][nx] == -2:
                vertDp[ny][nx] = dist + 1
                dq.append((nx,ny,False,dist+1))
        # 돌리기
        nx, ny = x - 1, y + 1
        if 0 <= nx < N and 0 <= ny < N and horiDp[ny][nx] == -2:
            if 0 <= x - 1 and vertDp[y][x-1] != -1 and x + 1 < N and vertDp[y][x+1] != -1:
                horiDp[ny][nx] = dist + 1
                dq.append((nx, ny, True, dist + 1))

if eHori and horiDp[ey][ex] != -2:
    print(horiDp[ey][ex])
elif (not eHori) and vertDp[ey][ex] != -2:
    print(vertDp[ey][ex])
else:
    print(0)
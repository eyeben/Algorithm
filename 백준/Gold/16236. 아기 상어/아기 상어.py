import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))

sx, sy = 0, 0
fishCnt = 0
for i in range(N):
    for j in range(N):
        num =li[i][j]
        if num == 9:
            sx, sy = j, i
            li[i][j]= 0
        elif num:
            fishCnt += 1


sharkSize = 2
sharkExp = 0

dx = [0,-1,1,0]
dy = [-1,0,0,1]
ans = 0
while fishCnt:
    dq = deque()
    dq.append((sx,sy,0))
    visited = [[False]*N for _ in range(N)]
    visited[sy][sx] = True
    tmp = []
    while dq:
        x,y,dis = dq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 범위 체크
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # 중복 탐색 방지
            if visited[ny][nx]:
                continue
            # 지나갈 수만 있는 경로
            if li[ny][nx] == sharkSize or li[ny][nx] == 0:
                visited[ny][nx] = True
                dq.append((nx,ny,dis+1))
            # 물코기 찾으면 추가
            elif li[ny][nx] < sharkSize:
                visited[ny][nx] = True
                tmp.append((nx,ny,dis+1))
    # 물고기 있으면 계산
    if tmp:
        fishCnt -= 1
        sharkExp += 1
        if sharkExp == sharkSize:
            sharkSize += 1
            sharkExp = 0
        tmp.sort(key = lambda x:x[0])
        tmp.sort(key = lambda x:x[1])
        tmp.sort(key = lambda x:x[2])

        nx, ny = tmp[0][0], tmp[0][1]
        sx,sy = nx,ny
        li[sy][sx] = 0
        ans += tmp[0][2]
    #없으면 종료
    else:
        print(ans)
        exit()
print(ans)
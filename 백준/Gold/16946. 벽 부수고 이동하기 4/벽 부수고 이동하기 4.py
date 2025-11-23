from collections import deque
N, M = map(int, input().split())
li = [list(map(int, list(input()))) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dic = {1: 0}
num = 2
for y in range(N):
    for x in range(M):
        if li[y][x] == 0:
            dq = deque([(x, y)])
            cnt = 1
            li[y][x] = num
            while dq:
                x1, y1 = dq.popleft()
                for i in range(4):
                    nx, ny = x1 + dx[i], y1 + dy[i]
                    if 0 <= nx < M and 0 <= ny < N and li[ny][nx] == 0:
                        li[ny][nx] = num
                        cnt += 1
                        dq.append((nx, ny))
            dic[num] = cnt
            num += 1

ans = [['0'] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if li[y][x] == 1:
            sett = set()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    sett.add(li[ny][nx])
            cnt = 1
            for itm in sett:
                cnt += dic[itm]
            ans[y][x] = str(cnt % 10)

for itm in ans:
    print(''.join(itm))
from collections import deque

N = int(input())
M = int(input())
bd = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    r,c = map(int,input().split())
    bd[r-1][c-1] = 2

L = int(input())
li = []
for _ in range(L):
    li.append(list(input().split()))

dx = [0,1,0,-1]
dy = [-1,0,1,0]
cmds = []
dir = 1
t0 = 0
for t,d in li:
    for _ in range(int(t) - t0):
        cmds.append(dir)
    t0 = int(t)
    if d == 'L':
        dir = (dir-1)%4
    elif d == 'D':
        dir = (dir + 1) % 4

for _ in range(N):
    cmds.append(dir)

q = deque()
q.append((0,0))
bd[0][0] = 1

def move(direction):
    head = list(q[-1])
    x = head[0] + dx[direction]
    y = head[1] + dy[direction]
    if 0<= x <N and 0<=y<N and bd[y][x]!=1:
        if bd[y][x] == 0:
            nx, ny = q.popleft()
            bd[ny][nx] = 0
        q.append((x, y))
        bd[y][x] = 1

        return True
    return False

for i in range(len(cmds)):
    if not move(cmds[i]):
        print(i+1)
        break
import sys
input = sys.stdin.readline
N, M = map(int,input().split())

li = []
for _ in range(N):
    li.append(list(input().strip()))

def nextNode(x,y):
    if li[y][x] == 'U':
        return (x,y-1)
    elif li[y][x] == 'D':
        return (x,y+1)
    elif li[y][x] == 'L':
        return (x-1,y)
    else:
        return (x+1,y)

isCycle = [[-1]*M for _ in range(N)]
cycleCnt = 0
for i in range(N):
    for j in range(M):
        if isCycle[i][j] != -1:
            continue
        nx,ny = j, i
        tmp = set()
        tmp.add((nx,ny))

        while True:
            nx,ny = nextNode(nx,ny)
            if isCycle[ny][nx]!=-1:
                break
            if (nx,ny) in tmp:
                cycleCnt += 1
                break
            tmp.add((nx, ny))


        for nx, ny in tmp:
            isCycle[ny][nx] = 1

print(cycleCnt)

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())

    li = []
    for _ in range(N):
        li.append(list(map(int, input().split())))

    ans = N

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    def man(sx,sy,dist):
        cnt = 0
        for i in range(max(0, sx-dist - 1), min(sx+dist+1, N)):
            for j in range(max(0,sy-dist), min(sy+dist+1,N)):
                if(abs(i-sx)+abs(j-sy) < dist):
                    cnt += li[j][i]
        return cnt

    mx = 0
    for dist in range(N+1,0,-1):
        goodFlag = False
        for i in range(N):
            for j in range(N):
                tmpcnt = man(j,i,dist)
                if tmpcnt * M >= dist**2 + (dist-1)**2:
                    goodFlag = True
                    mx = max(mx, tmpcnt)
        if goodFlag:
            break
    print("#%d %d" % (tc, mx))



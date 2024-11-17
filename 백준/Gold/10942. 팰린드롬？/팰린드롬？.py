import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))
M = int(input())
li2 = []
for _ in range(M):
    li2.append(sorted(list(map(int,input().split()))))

isPiland = [[False]* N for _ in range(N)]

for idx in range(N):
    isPiland[idx][idx] = True
    for i in range(N):
        left = idx - i
        right =idx+i
        if(left < 0 or right>=N):
            break
        if(li[left] != li[right]):
            break
        isPiland[left][right] = True

for idx in range(N-1):
    for i in range(N):
        left = idx - i
        right =idx+1+i
        if(left < 0 or right>=N):
            break
        if(li[left] != li[right]):
            break
        isPiland[left][right] = True

for i in range(M):
    if isPiland[li2[i][0]-1][li2[i][1]-1]:
        print(1)
    else:
        print(0)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = [[ 0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    tmp = list(map(int,list(input().strip())))
    for j in range(M):
        li[i+1][j+1] = tmp[j]
ans = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if li[i][j]:
            li[i][j] = min(li[i-1][j], li[i][j-1], li[i-1][j-1]) + 1
            ans = max(li[i][j], ans)

print(ans**2)
import sys
input = sys.stdin.readline
N, H = map(int, input().split())
cntU = [0]*H
cntD = [0]*H

for i in range(N):
    n = int(input()) - 1
    if i%2 == 0:
        cntU[n] += 1
    else:
        cntD[H - 1 - n] += 1

for i in range(H-1 -1, -1, -1):
    cntU[i] += cntU[i+1]
for i in range(H-1):
    cntD[i+1] += cntD[i]

view = [0] * H
for i in range(H):
    view[i] = cntU[i]+cntD[i]
ans1 = min(view)
ans2 = view.count(ans1)
print(ans1, ans2)
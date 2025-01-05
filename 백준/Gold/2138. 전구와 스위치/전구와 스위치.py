N = int(input())
start = input()
goal = list(map(int,input()))

if goal == start:
    print(0)
    exit(0)

start1 = list(map(int, start))
start2 = [(start1[0]+1)%2, (start1[1]+1)%2]+start1[2:]
anss = []
cnt1 = 0
for i in range(N-2):
    if start1[i] == goal[i]:
        continue
    start1[i] = (start1[i] + 1) % 2
    start1[i+1] = (start1[i+1] + 1) % 2
    start1[i+2] = (start1[i+2] + 1) % 2
    cnt1 += 1
if start1[-2] == goal[-2] and start1[-1] == goal[-1]:
    anss.append(cnt1)
elif start1[-2] != goal[-2] and start1[-1] != goal[-1]:
    anss.append(cnt1+1)

cnt2 = 1
for i in range(N-2):
    if start2[i] == goal[i]:
        continue
    start2[i] = (start2[i] + 1) % 2
    start2[i+1] = (start2[i+1] + 1) % 2
    start2[i+2] = (start2[i+2] + 1) % 2
    cnt2 += 1

if start2[-2] == goal[-2] and start2[-1] == goal[-1]:
    anss.append(cnt2)
elif start2[-2] != goal[-2] and start2[-1] != goal[-1]:
    anss.append(cnt2+1)

if anss:
    print(min(anss))
else:
    print(-1)
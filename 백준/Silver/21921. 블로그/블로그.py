N, X = map(int, input().split())
li1 = list(map(int, input().split()))

li2 = [0]
for itm in li1:
    li2.append(li2[-1] + itm)

mx = 0
cnt = 1
for i in range(N - X+1):
    newMx = li2[i+X] - li2[i]
    if mx == newMx:
        cnt += 1
    elif mx < newMx:
        cnt = 1
        mx = newMx
if mx == 0:
    print("SAD")
else:
    print(mx)
    print(cnt)
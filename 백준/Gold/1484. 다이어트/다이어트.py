N = int(input())
ans = []
for i in range(1,N):
    if N%i == 0:
        a = i
        b = N//i
        if a >= b:
            break
        if (a+b)%2 == 0:
            ans.append((a+b)//2)
ans.reverse()
if not ans:
    ans.append(-1)
for itm in ans:
    print(itm)
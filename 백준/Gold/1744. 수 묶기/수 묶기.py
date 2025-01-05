N = int(input())
plus = []
minus = []
zero = 0
for _ in range(N):
    n = int(input())
    if n>0:
        plus.append(n)
    elif n<0:
        minus.append(n)
    else:
        zero += 1

plus.sort()
minus.sort(reverse=True)

ans = 0

while len(plus)>=2:
    a = plus.pop(-1)
    b = plus.pop(-1)
    if a*b > a+b:
        ans += a*b
    else:
        ans += a+b


while len(minus)>=2:
    a = minus.pop(-1)
    b = minus.pop(-1)
    if a*b > a+b:
        ans += a*b
    else:
        ans += a+b

if zero>0:
    ans += sum(plus)
else:
    ans += sum(plus) + sum(minus)

print(ans)
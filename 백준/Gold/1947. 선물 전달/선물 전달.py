N = int(input())
d1=0
d2=1
for i in range(2,N):
    tmp = (i*(d1+d2))%int(1e9)
    d1 = d2
    d2 = tmp
if N == 1:
    d2 =0
print(d2)
N, S, M = map(int,input().split())

li = list(map(int, input().split()))

a = set()
a.add(S)

for i in li:
    b = set()
    for itm in list(a):
        if itm+i <= M:
            b.add(itm+i)
        if 0<= itm - i:
            b.add(itm-i)
    if len(b) == 0:
        print(-1)
        exit()
    a = b

print(max(a))

N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int,input().split())))

dp = set()
dp.add((1,0))

for s,b in li:
    for ds, db in list(dp):
        dp.add((ds*s,db+b))

dp.remove((1,0))

node = min(list(dp), key = lambda x:abs(x[0]-x[1]))
print(abs(node[0]- node[1]))
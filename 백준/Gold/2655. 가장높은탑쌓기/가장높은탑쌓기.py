N = int(input())
li = []
for i in range(1, N+1):
    li.append(list(map(int,input().split()))+[i])
li.sort(reverse=True)

vals = [li[i][1] for i in range(N)]
anss = [[li[i][3]] for i in range(N)]
for i in range(N):
    for j in range(i):
        if li[j][2] > li[i][2] and vals[j] + li[i][1] > vals[i]:
            vals[i] = vals[j] + li[i][1]
            anss[i] = anss[j] + [li[i][3]]

idx = vals.index(max(vals))
print(len(anss[idx]))
for i in range(len(anss[idx])-1,-1,-1):
    print(anss[idx][i])

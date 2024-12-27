N, M = map(int,input().split())
li = []
for _ in range(M):
    a,b,c = map(int,input().split())
    li.append((a, b, c))

BIG  = int(1e9)
dists = [BIG]*(N+1)
dists[1] = 0
def ford():
    for i in range(N):
        for j in range(M):
            a = li[j][0]
            b = li[j][1]
            c = li[j][2]

            if dists[a] != BIG and dists[b] > dists[a] + c:
                dists[b] = dists[a] + c
                if i == N - 1:
                    return True
    return False

if ford():
    print(-1)
else:
    for i in range(2,N+1):
        if dists[i] == BIG:
            print(-1)
        else:
            print(dists[i])
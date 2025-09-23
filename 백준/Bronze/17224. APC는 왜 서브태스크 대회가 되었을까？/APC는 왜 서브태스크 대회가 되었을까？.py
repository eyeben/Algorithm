N,L,K=map(int,input().split())
q=[]
ans=0
for _ in range(N):
    q.append(list(map(int, input().split())))
for i in range(K):
    if q[i][1]<=L:
        ans+=140
    elif q[i][0]<=L:
        ans+=100
    else:
        break
print(ans)
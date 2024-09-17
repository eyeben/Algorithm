N = int(input())
parents = [i for i in range(27)]
for _ in range(N):

    a,b = map(ord, input().split(" is "))
    parents[a-ord('a')] = b-ord('a')

M = int(input())

anss = []
for _ in range(M):
    tmp1,tmp2 = map(ord,input().split(" is "))
    a = tmp1 -ord('a')
    b = tmp2 -ord('a')
    ans = 'F'
    while parents[a] != a:
        if parents[a] == b:
            ans = 'T'
            break
        a = parents[a]
    anss.append(ans)

print('\n'.join(anss))
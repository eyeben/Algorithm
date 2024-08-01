import sys
N = int(sys.stdin.readline())
parents = [i for i in range(N+1)]

def find(child):
    if child == parents[child]:
        return child
    return find(parents[child])

def union(lhs, rhs):
    l = find(lhs)
    r = find(rhs)
    
    if l == r:
        return
    elif l > r:
        parents[l] = r
    else:
        parents[r] = l

netLength = int(sys.stdin.readline())
for i in range(netLength):
    lhs, rhs = map(int,sys.stdin.readline().split())
    union(lhs, rhs)

cnt = 0
for item in parents:
    if find(item) == 1:
        cnt+=1
print(cnt - 1)
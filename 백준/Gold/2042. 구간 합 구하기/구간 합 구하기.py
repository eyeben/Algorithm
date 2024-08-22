N,M,K = map(int, input().split())
size = 1
while size < N:
    size <<= 1
tree = [0]*(2*size)
size -= 1


def update(idx,val):
    idx += size
    while idx:
        tree[idx] += val
        idx //= 2


def query(left, right):
    total = 0
    left += size
    right += size

    while left<= right:
        if left%2 == 1:
            total += tree[left]
            left += 1
        left //= 2
        if right%2 == 0:
            total += tree[right]
            right -= 1
        right //= 2
    return total


for i in range(1, N+1):
    update(i, int(input()))

ans = []
for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        update(b, c-tree[size+b])
    else:
        ans.append(query(b,c))

for itm in ans:
    print(itm)
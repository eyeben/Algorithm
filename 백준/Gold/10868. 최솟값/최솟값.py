import sys
input = sys.stdin.readline

mii = lambda: map(int, input().split())
N, M = mii()
BIG = 1e9+1

size = 1
while size<N:
    size <<= 1
tree = [BIG] * (size*2)
size -= 1

def update(idx, val):
    idx += size
    tree[idx] = val
    while idx:
        if idx % 2 == 0:
            tree[idx//2] = min(tree[idx], tree[idx+1])
        else:
            tree[idx//2] = min(tree[idx], tree[idx-1])
        idx //= 2

def query(left, right):
    left += size
    right += size
    mn = BIG
    while left <= right:
        if left % 2 == 1:
            mn = min(mn,tree[left])
            left += 1
        left //= 2

        if right % 2 == 0:
            mn = min(mn, tree[right])
            right -= 1

        right //= 2
    return mn

for i in range(1, N+1):
    update(i, int(input()))

ans = []
for _ in range(M):
    left, right = mii()
    ans.append(str(query(left, right)))
print('\n'.join(ans))
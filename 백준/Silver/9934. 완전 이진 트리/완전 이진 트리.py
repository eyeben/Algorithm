N = int(input())

li = list(map(int, input().split()))
tree = [0] * 2 ** N
idx = 0
def dfs(treeidx):
    global idx
    if treeidx >= 2**N:
        return
    dfs(treeidx*2)
    tree[treeidx] = li[idx]
    idx += 1
    dfs(treeidx*2+1)

dfs(1)
size = 1
idx = 1
while idx < 2**N:
    for _ in range(size):
        print(tree[idx], end = ' ')
        idx += 1
    size *= 2
    print()
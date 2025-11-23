N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

mark = [False] * (N * 2 - 1)


def dfs(n, k):
    global mx
    if n >= 2 * N - 1:
        mx = max(mx, k)
        return
    dfs(n + 2, k)
    if n < N:
        x, y = 0, n
    else:
        x, y = n - (N - 1), N - 1

    piv = (N * 2 - 1) // 2 - n if n < N else n - (N - 1)

    while 0 <= x < N and 0 <= y < N:
        if li[y][x] == 1 and not mark[piv]:
            mark[piv] = True
            li[y][x] = 2
            dfs(n + 2, k + 1)
            li[y][x] = 1
            mark[piv] = False
        piv += 2
        x += 1
        y -= 1


mx = 0
dfs(0, 0)
mx1 = mx

mx = 0
dfs(1, 0)
mx2 = mx

print(mx1 + mx2)

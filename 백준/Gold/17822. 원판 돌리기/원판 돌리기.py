from collections import deque

N, M, T = map(int, input().split())
li = []
for _ in range(N):
    li.append(deque(list(map(int, input().split()))))


def rotate(x, d, k):
    nx = x
    if d:
        while nx <= N:
            for _ in range(k):
                li[nx - 1].append(li[nx - 1].popleft())
            nx += x
    else:
        while nx <= N:
            for _ in range(k):
                li[nx - 1].appendleft(li[nx - 1].pop())
            nx += x


def markpop():
    for i in range(N):
        for j in range(M - 1):
            if li[i][j] == li[i][j + 1] and li[i][j]:
                popmark[i][j] = True
                popmark[i][j + 1] = True
        if li[i][0] == li[i][-1] and li[i][0]:
            popmark[i][0] = True
            popmark[i][-1] = True

    for i in range(M):
        for j in range(N - 1):
            if li[j][i] == li[j + 1][i] and li[j][i]:
                popmark[j][i] = True
                popmark[j + 1][i] = True

    badflag = True
    for i in range(N):
        for j in range(M):
            if popmark[i][j]:
                badflag = False
                li[i][j] = 0

    if badflag:
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if li[i][j]:
                    cnt += 1
                    total += li[i][j]

        if cnt == 0:
            return

        val = total / cnt
        for i in range(N):
            for j in range(M):
                if li[i][j] and li[i][j] > val:
                    li[i][j] -= 1
                elif li[i][j] and li[i][j] < val:
                    li[i][j] += 1


for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    popmark = [[False] * M for _ in range(N)]
    markpop()

ans = 0
for itms in li:
    ans += sum(itms)
print(ans)
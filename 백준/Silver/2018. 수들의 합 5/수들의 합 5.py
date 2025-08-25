N = int(input())
ans = 1
start = 1
end = 2
cur = 3
while start < end < N:
    if cur == N:
        ans += 1
        end += 1
        cur += end
    elif cur < N:
        end += 1
        cur += end
    else:
        cur -= start
        start += 1
print(ans)
T = int(input())

for tc in range(T):
    N = int(input())
    li = []
    for _ in range(N):
        li.append(input())

    li.sort(key=lambda x: len(x))
    li.sort()

    ans = "YES"
    for i in range(N-1):
        if li[i] == li[i+1][:len(li[i])]:
            ans = "NO"
            break
    print(ans)
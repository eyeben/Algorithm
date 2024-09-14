T = int(input())

for tc in range(T):
    N = int(input())
    li = []
    for _ in range(N):
        li.append(input())
		# 정렬 2번 수행
    li.sort()
		# 포함 관계인지 체크 후 출력
    ans = "YES"
    for i in range(N-1):
        if li[i] == li[i+1][:len(li[i])]:
            ans = "NO"
            break
    print(ans)
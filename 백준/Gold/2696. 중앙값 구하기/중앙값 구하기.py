import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    li = []
    for _ in range((N-1)//10 + 1):
        li += list(map(int, input().split()))
    left =[-li[0]] # 여기 틀렸음
    right = []
    ans = [li[0]]
    for i in range(1, N):
        num = li[i]
        if -left[0] < num:
            heapq.heappush(right, num)
        else:
            heapq.heappush(left, -num)

        if i%2 == 0:
            while len(left) < len(right)+1:
                heapq.heappush(left, -heapq.heappop(right))
            while len(right)+1 < len(left):
                heapq.heappush(right, -heapq.heappop(left))

            ans.append(-left[0])
    print(len(ans))
    print(*ans)
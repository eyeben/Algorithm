def check(stones, k, mid):
    cnt = 0
    for stone in stones:
        if stone - mid < 0:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    start = 1
    end = max(stones)  # 최대 돌 개수로 제한
    ans = start

    while start <= end:
        mid = (start + end) // 2
        if check(stones, k, mid):  # 건널 수 있음
            ans = mid  # 현재 mid 값 저장
            start = mid + 1  # 더 큰 mid 값을 찾아봄
        else:  # 건널 수 없음
            end = mid - 1  # mid 값을 줄여야 함

    return ans

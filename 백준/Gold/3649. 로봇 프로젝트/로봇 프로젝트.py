while True:
    try:
        x = int(input())*10000000
        n = int(input())
        arr = [int(input()) for _ in range(n)]
        arr.sort()
        answer = []
        left, right = 0, n-1
        while left < right:
            if arr[left]+arr[right] < x:
                left += 1
            elif arr[left]+arr[right] > x:
                right -= 1
            else:
                answer = [arr[left], arr[right]]
                break
        if answer:
            print('yes {0} {1}'.format(answer[0], answer[1]))
        else:
            print('danger')
    except:
        break
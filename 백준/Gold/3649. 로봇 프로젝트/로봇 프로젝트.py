import sys
input = sys.stdin.readline

while True:
    try:
        X = int(input())*10**7
        N = int(input())
        li = []
        for _ in range(N):
            li.append(int(input()))

        li.sort()
        left = 0
        right = N - 1
        goodFlag = False
        while left<right:
            piv = li[left] + li[right]
            if piv < X:
                left += 1
            elif X < piv:
                right -= 1
            else:
                print("yes", li[left], li[right])
                goodFlag = True
                break
        if not goodFlag:
            print("danger")
    except:
        break
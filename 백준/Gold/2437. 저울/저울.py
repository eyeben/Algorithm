N = int(input())
li = list(map(int, input().split()))

li.sort()

nu = 1

for itm in li:
    if nu < itm:
        break
    nu += itm


print(nu)
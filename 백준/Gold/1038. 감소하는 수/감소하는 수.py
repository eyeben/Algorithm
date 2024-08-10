MAX_NUM = 9876543210
N = int(input())
li = [i for i in range(10)]
head = 1
digit = 2

def fillUp():
    global head, digit
    dfs(head*10**(digit-1), digit-1)
    if head == 9:
        head, digit = 1, digit+1
    else:
        head += 1

def dfs(num, digitToFill):
    if digitToFill == 0:
        li.append(num)
        return

    head = int(str(num)[-digitToFill-1])

    if head == 0:
        return

    for i in range(head):
        nNum = num - num%10**digitToFill + i*10**(digitToFill-1)
        dfs(nNum,digitToFill-1)

head = 1
digit = 2
while len(li)<N+1:
    if li[-1] == MAX_NUM:
        print(-1)
        exit(0)
    fillUp()

print(li[N])
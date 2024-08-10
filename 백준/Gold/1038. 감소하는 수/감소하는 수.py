MAX_NUM = 9876543210
N = int(input())
# li에는 순서대로 구해진 값을 저장, 9까지는 직접 저장
li = [i for i in range(10)]
# head는 맨 앞자리 숫자, digit은 전체 자리수
head = 1
digit = 2

# dfs를 이용하여 li에 값을 채운다. head값이 상승하기 전까지
def fillUp():
    global head, digit
    dfs(head*10**(digit-1), digit-1)
    if head == 9:
        head, digit = 1, digit+1
    else:
        head += 1

# dfs를 이용하여 li에 값을 채움
def dfs(num, digitToFill):
    # 0자리 수 까지 도달 했다면 li에 값을 추가
    if digitToFill == 0:
        li.append(num)
        return

    # ahead는 앞자리 수, 0이면 안됨
    ahead = int(str(num)[-digitToFill-1])
    if ahead == 0:
        return
    # nNum 만들고 채워야 할 자리숫자 줄이고 재귀 들어감 
    for i in range(ahead):
        nNum = num - num%10**digitToFill + i*10**(digitToFill-1)
        dfs(nNum,digitToFill-1)

# 반복문을 통해 li를 매꾼다
while len(li)<N+1:
    if li[-1] == MAX_NUM:
        print(-1)
        exit(0)
    fillUp()

print(li[N])
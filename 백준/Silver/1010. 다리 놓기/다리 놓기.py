for _ in range(int(input())):
    b, a  = map(int, input().split())
    n1 = 1
    n2 = 1
    for i in range(a-b + 1, a + 1):
        n1 *= i
    for i in range(1, b+1):
        n2 *= i
    print(n1//n2)
def solution(n, w, num):
    num -= 1
    n -= 1

    y1 = num // w
    y2 = n // w
    if y1 == y2:
        return 1
    
    tmp = 0
    x1 = num % w
    x2 = n % w
    
    if y1 % 2:
        x1 = w - 1 - (num % w)
        
    if y2 % 2:
        x2 = w - 1 - (n % w)
        tmp = x2 <= x1
    else:
        tmp = x1 <= x2
    print(tmp)
    return y2 - y1 + tmp

def solution(N, number):
    if N == number:
        return 1
    yunsan = ["*","//","+","-"]
    li = [{},{N}]
    for i in range(2, 9):
        tmp = {int(str(N)*i)}
        for j in range(1,i):
            for itm1 in li[j]:
                for itm2 in li[i-j]:
                    for itm3 in yunsan:
                        if eval(str(itm1)+itm3+str(itm2)):
                            tmp.add(eval(str(itm1)+itm3+str(itm2)))
        if number in tmp:
            return(i)
        li.append(tmp)
                    
    return -1
import re
def solution(today, terms, privacies):
    dic = dict()
    for itm in terms:
        tmp = itm.split()
        dic[tmp[0]] = int(tmp[1])
    li = []
    for i in range(len(privacies)):
        tmp = re.split(r'[. ]', privacies[i])
        li.append(int(tmp[0])*12*28 + int(tmp[1])*28 + int(tmp[2]) + dic[tmp[3]]* 28)
    tmp = list(map(int, today.split('.')))
    now = tmp[0]*12*28+tmp[1]*28 + tmp[2]
    ans=[]
    for i in range(len(li)):
        if li[i] <= now:
            ans.append(i+1)
    return ans
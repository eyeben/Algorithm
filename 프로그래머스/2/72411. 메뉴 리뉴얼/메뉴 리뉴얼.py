from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    dd = defaultdict(int)
    for itm in orders:
        word = sorted(itm)
        for i in range(2, len(word) + 1):
            for itm2 in list(combinations(word, i)):
                dd[''.join(itm2)] += 1
    print(dd)
    len_to_cnt = defaultdict(int)
    kys = dd.keys()
    for k, v in dd.items():
        len_to_cnt[len(k)] = max(len_to_cnt[len(k)], v)
    print(len_to_cnt)
    
    anss = []
    for itm in course:
        cnt = len_to_cnt[itm]
        for k in kys:
            if len(k) == itm and dd[k] == cnt >= 2:
                anss.append(k)
        
    return sorted(anss)
    
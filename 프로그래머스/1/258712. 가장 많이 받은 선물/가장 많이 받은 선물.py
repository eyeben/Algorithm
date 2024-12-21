from itertools import combinations
from collections import defaultdict
def solution(friends, gifts):
    jisu = defaultdict(int)
    comb = list(combinations(friends,2))
    counts = defaultdict(int)
    
    for itms in gifts:
        a,b = itms.split()
        jisu[a] += 1
        jisu[b] -= 1
    
    for a,b in comb:
        cntA = gifts.count(a+" "+b)
        cntB = gifts.count(b+" "+a)
        if cntA>cntB:
            counts[a] += 1
        elif cntA<cntB:
            counts[b] += 1
        else:
            if jisu[a] < jisu[b]:
                counts[b] += 1
            elif jisu[a] > jisu[b]:
                counts[a] += 1
    anss = (dict(counts).values())
    ans = 0
    if anss:
        ans = max(anss)

    return ans
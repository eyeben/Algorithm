from collections import deque

def solution(cacheSize, cities):
    cities = [itm.upper() for itm in cities]
    dq = deque()
    ans = 0
    for itm in cities:
        if itm not in dq:
            dq.append(itm)
            while len(dq) > cacheSize:
                dq.popleft()
            ans += 5
        else:
            ndq = deque()
            while dq:
                word = dq.popleft()
                if word == itm:
                    continue
                ndq.append(word)
            ndq.append(itm)
            dq = ndq
            ans += 1
    return ans

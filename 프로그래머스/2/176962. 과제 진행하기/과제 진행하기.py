def solution(plans):
    plans = [[itms[0], int(itms[1].split(":")[0]) * 60 + int(itms[1].split(":")[1]), int(itms[2])] for itms in plans]
    plans.sort(key = lambda x:x[1])
    stk = [plans[0]]
    anss = []
    for name2, start2, dur2 in plans[1:]:
        name, start, dur = stk[-1]
        usableTime = start2 - start
        while stk:
            name, start, dur = stk[-1]
            if usableTime >= dur:
                usableTime -= dur
                anss.append(name)
                stk.pop()
            else:
                stk[-1][2] -= usableTime
                break
        stk.append([name2,start2,dur2])

    stk.reverse()
    anss2 = [itm[0] for itm in stk]

    return anss + anss2
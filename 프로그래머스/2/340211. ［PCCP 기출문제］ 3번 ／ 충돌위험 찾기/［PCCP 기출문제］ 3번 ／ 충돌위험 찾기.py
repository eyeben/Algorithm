def solution(points, routes):
    points = [[itm[0]-1, itm[1]-1] for itm in points]
    routes = [[n-1 for n in itm] for itm in routes]
    
    def getRoute(route):
        ans = []
        prevNum = route[0]
        for nextNum in route[1:]:
            
            prevY, prevX = points[prevNum]
            nextY, nextX = points[nextNum]
            
            piv = 1
            if nextY < prevY:
                piv = -1
            while prevY != nextY:
                ans.append((prevY, prevX))
                prevY += piv
                
            piv = 1
            if nextX < prevX:
                piv = -1
            while prevX != nextX:
                ans.append((prevY, prevX))
                prevX += piv
            prevNum = nextNum
        ans.append(tuple(points[nextNum]))
        return ans
    
    anss = []
    L = 0
    for itm in routes:
        anss.append(getRoute(itm))
        L = max(L, len(anss[-1]))
    cnt = 0
    for i in range(L):
        set1 = set()
        set2 = set()
        for j in range(len(anss)):
            if len(anss[j]) - 1 < i:
                continue
            if anss[j][i] in set1:
                set2.add(anss[j][i])
            else:
                set1.add(anss[j][i])
        cnt += len(set2)

        
        
    return cnt
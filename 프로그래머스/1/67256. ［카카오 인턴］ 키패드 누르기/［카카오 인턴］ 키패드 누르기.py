def solution(numbers, hand):
    coord = dict()
    for i in range(12):
        coord[i + 1] = (i // 3, i % 3)
    coord[0] = coord[11]
    left = 10
    right = 12
    ans = []
    for itm in numbers:
        if itm in (3,6,9):
            ans.append('R')
            right = itm
            continue
            
        elif itm in (1,4,7):
            ans.append('L')
            left = itm
            continue
        
        ld = abs(coord[left][0] - coord[itm][0]) + abs(coord[left][1] - coord[itm][1])
        rd = abs(coord[right][0] - coord[itm][0]) + abs(coord[right][1] - coord[itm][1])
        if rd < ld or (ld == rd and hand == 'right'):
            ans.append('R')
            right = itm
        else:
            ans.append('L')
            left = itm
    return ''.join(ans)
    answer = ''
    return answer
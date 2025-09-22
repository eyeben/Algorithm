from itertools import combinations_with_replacement
N, M = map(int, input().split())
li = [ i for i in range(1, N + 1)]
for itms in list(combinations_with_replacement(li, M)):
    print(*itms)

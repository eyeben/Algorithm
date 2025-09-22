N = int(input())
li = [input() for _ in range(N)]
ans = input().split()

dic = dict()

for idx, itm in enumerate(ans):
    dic[itm] = idx


def is_asc(arr):
    if arr[0] in dic:
        num = dic[arr[0]]
        for itm in arr[1:]:
            if not (itm in dic and num < dic[itm]):
                return False
            num = dic[itm]
        return True
    return False


visited = [False] * len(ans)
for itm in li:
    tmp = itm.split()
    if is_asc(tmp):
        for word in tmp:
            visited[dic[word]] = True

print('Possible' if all(visited) else 'Impossible')

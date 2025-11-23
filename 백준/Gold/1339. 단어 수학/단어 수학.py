from collections import defaultdict
dd = defaultdict(int)
for _ in range(int(input())):
    word = input()
    num = 1
    for itm in word[::-1]:
        dd[itm] += num
        num *= 10

li = sorted(list(dd.items()), key=lambda x:x[1], reverse=True)
ans = 0
for i in range(min(10, len(li))):
    ans += (9-i) * li[i][1]
print(ans)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(M)]


parents = [i for i in range(N + 1)]

def get_parent(n):
    if n != parents[n]:
        parents[n] = get_parent(parents[n])
    return parents[n]

def union(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b:
        parents[b] = a
    elif b < a:
        parents[a] = b

li.sort(key = lambda x: x[-1])
ans = 0
last = 0
for a,b,c in li:
    if get_parent(a) != get_parent(b):
        union(a, b)
        ans += c
        last = c

print(ans - last)
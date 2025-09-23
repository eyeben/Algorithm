N, L, D = map(int, input().split())

cur = 0
phone = 0
for _ in range(N):
    cur += L
    while phone < cur:
        phone += D
    if cur <= phone < cur + 5:
        print(phone)
        exit(0)
    cur += 5
print(phone)
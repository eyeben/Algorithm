import sys

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []

# 모든 A+B 경우
for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])

# 모든 C+D 경우
for i in range(N):
    for j in range(N):
        CD.append(C[i] + D[j])

# AB는 오름차순, CD는 내림차순 정렬
AB.sort()
CD.sort(reverse=True)

ans = 0
i, j = 0, 0
len_AB = len(AB)
len_CD = len(CD)

while i < len_AB and j < len_CD:
    temp = AB[i] + CD[j]
    if temp == 0:
        # AB[i] 값이 같은 것 몇개인지 세기
        a_val = AB[i]
        a_cnt = 0
        while i < len_AB and AB[i] == a_val:
            a_cnt += 1
            i += 1

        # CD[j] 값이 같은 것 몇개인지 세기
        c_val = CD[j]
        c_cnt = 0
        while j < len_CD and CD[j] == c_val:
            c_cnt += 1
            j += 1

        ans += a_cnt * c_cnt

    elif temp < 0:
        i += 1
    else:
        j += 1

print(ans)

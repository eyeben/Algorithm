A, B = map(int, input().split())
big, small = max(A,B), min(A,B)
while small:
    big, small = small, big % small

print('1'*big)


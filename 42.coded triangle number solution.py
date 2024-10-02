from math import sqrt
for _ in range(int(input())):
    n = int(input())
    s = sqrt(1+8*n)
    if s % 2 == 1:
        print(int((s - 1) // 2))
    else:
        print(-1)

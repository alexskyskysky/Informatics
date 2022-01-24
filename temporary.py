from math import sqrt, ceil


def F(n):
    count = 0
    L = ceil(sqrt(n))
    for d in range(2, L):
        if n % d == 0:
            count += 2
    if sqrt(n).is_integer():
        count -= 1
    return count == 6


count = 0
min_n = 100000000
for N in range(50000000, 60000001):
    if N % 911 == 0:
        if F(N):
            count += 1
            if N < min_n:
                min_n = N
print(count, min_n)

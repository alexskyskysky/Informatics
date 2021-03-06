# Вариант 1 (2021)
from math import ceil, sqrt


def F(N):
    L = ceil(sqrt(N))  # последнее число в диапазоне проверки
    for k in range(2, L + 1):
        if N % k == 0:
            return N // k - k
    return 0


count = 0
N = 850001
while count < 6:
    f = F(N)
    if f != 0 and f % 7 == 0:
        count += 1
        print(N, f)
    N += 1

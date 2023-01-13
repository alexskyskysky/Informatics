from math import ceil, sqrt


def isCorrect(n):
    count = 0
    for d in range(2, ceil(sqrt(n))):
        if n % d == 0:
            count += 2
    if sqrt(n).is_integer():
        count -= 1
    return count == 6


count = 0
min_n = 0
for x in range(50000000, 60000001):
    if x % 911 == 0 and isCorrect(x):
        count += 1
        if count == 1:
            min_n = x
print(count, min_n)

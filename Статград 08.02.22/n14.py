N = 5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98
Counts = [0] * 7
while N > 0:
    Counts[N % 7] += 1
    N //= 7
print(Counts.index(max(Counts)))

from math import log2, ceil

n = (24 * 1024 * 1024 * 8) // (320 * 240 * ceil(log2(256)))
print(n)

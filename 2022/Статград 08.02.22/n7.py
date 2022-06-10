from math import log2, ceil

count = (27 * 1024 * 1024 * 8) // (320 * 240 * ceil(log2(256)))  # сколько раз можно записать за 1 час
n = ceil(3600 / count)
print(n)

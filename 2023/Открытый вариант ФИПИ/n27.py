from math import ceil

f = open("C:\\ЕГЭ\\ЕГЭ-23\\Вариант Открытый ФИПИ 1\\Файлы\\27_B.txt")
n = int(f.readline())
A = []
for i in range(n):
    k, p = map(int, f.readline().split())
    c = ceil(p / 44)
    A.append([k, c])
f.close()
A.sort()

B = [0] * n
B[0] = A[0][1]
for i in range(1, n):
    B[i] = B[i - 1] + A[i][1]

s = 0
for i in range(n):
    s += abs(A[0][0] - A[i][0]) * A[i][1]

min_sum = s

for i in range(1, n):
    d = abs(A[i][0] - A[i - 1][0])
    s += d * B[i - 1] - d * (B[n - 1] - B[i - 1])
    if s < min_sum:
        min_sum = s
print(min_sum)

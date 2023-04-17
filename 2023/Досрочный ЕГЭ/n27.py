f = open("C:\\ЕГЭ\\ЕГЭ-23\\Досрочный вариант\\Файлы\\27B.txt")
n = int(f.readline())
k = int(f.readline())
M = []
for line in f:
    M.append(int(line))
f.close()

maxK = 0
maxSum = 0
for i in range(k, n):
    if M[i - k] > maxK:
        maxK = M[i - k]
    if M[i] + maxK > maxSum:
        maxSum = M[i] + maxK
print(maxSum)

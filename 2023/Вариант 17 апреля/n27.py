f = open("C:\\ЕГЭ\\ЕГЭ-23\\Вариант 17 апреля\\Файлы\\27B.txt")
k = int(f.readline())
n = int(f.readline())
N = []
for i in range(n):
    N.append(int(f.readline()))
f.close()

D = [0] * k
s = 0
maxS = 0
for i in range(1, n):
    s = (s + N[i - 1]) % k
    if D[s] != 0 and D[s] + N[i] > maxS:
        maxS = D[s] + N[i]
    if N[i - 1] > D[s]:
        D[s] = N[i - 1]
print(maxS)

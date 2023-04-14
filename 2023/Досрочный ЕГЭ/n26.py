f = open("C:\\ЕГЭ\\ЕГЭ-23\\Досрочный вариант\\Файлы\\26.txt")
k = int(f.readline())
n = int(f.readline())
P = []
for i in range(n):
    start, end = map(int, f.readline().split())
    P.append([start, end])
f.close()

count = 0
last = -1
Cam = [0] * k
for i in range(n):
    for j in range(k):
        if P[i][0] > Cam[j]:
            count += 1
            Cam[j] = P[i][1]
            last = j + 1
            break
print(count, last)

# Вариант 12 (2022)
WomanId = []
f = open("C:\\ЕГЭ\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 12\\Задание 3\\3_1.txt", "r")
for line in f:
    WomanId.append(int(line))
f.close()
Id = []
Price = []
f = open("C:\\ЕГЭ\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 12\\Задание 3\\3_2.txt", "r")
for line in f:
    a, b, c = map(int, line.split())
    Id.append(a)
    Price.append(c)
f.close()

S = 0
for i in range(len(Id)):
    if Id[i] in WomanId:
        S += Price[i]
print(S)

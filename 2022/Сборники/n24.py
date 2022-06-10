# Вариант 1 (2022)
f = open("C:\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 1\\Задание 24\\24.txt", "r")
t = f.read()
f.close()

X = [0] * 4
for i in range(2, len(t)):
    if t[i - 1] == "A" and t[i] == "D":
        X[ord(t[i - 2]) - ord("A")] += 1
print(X)

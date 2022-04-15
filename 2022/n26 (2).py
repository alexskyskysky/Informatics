# Вариант 1 (2022 - сборник 20 вариантов)
f = open("D:\\ЕГЭ\\ЕГЭ-22\\Сборник 20 вариантов\\26\\input26_01.txt", "r")
N = int(f.readline())
Pixels = []
for _ in range(N):
    row, column = map(int, f.readline().split())
    Pixels.append([row, column])
f.close()
Pixels.sort(reverse=True)
min_column = 100000
i = 1
while not (Pixels[i][0] == Pixels[i - 1][0] and abs(Pixels[i][1] - Pixels[i - 1][1]) == 3):
    i += 1
max_row = Pixels[i][0]
min_column = Pixels[i][1] + 1
while Pixels[i][0] == max_row:
    if abs(Pixels[i][1] - Pixels[i - 1][1]) == 3:
        min_column = Pixels[i][1] + 1
    i += 1
print(max_row, min_column)

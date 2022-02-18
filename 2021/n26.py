# Вариант 1 (2021)
with open("D:\\ЕГЭ\\ЕГЭ-21\\26\\input26_01.txt", "r") as f:
    S, N = map(int, f.readline().split())
    Files = []
    for i in range(N):
        Files.append(int(f.readline()))

Files.sort()
count = 0
max_file = 0
i = 0
while S > 0 and i < len(Files):  # пока есть место на диске и пока остались файлы
    S -= Files[i]
    count += 1
    max_file = Files[i]
    i += 1
if i == len(Files):  # если закончились файлы
    if S >= 0:  # если при этом осталось место на диске
        print(count, max_file)
    else:  # если при этом закончилось место на диске
        # определяем, какой из последних двух файлов мог поместиться
        max_file = Files[i - 1] if S + Files[i - 1] + Files[i - 2] >= Files[i - 1] else Files[i - 2]
        print(count, max_file)
else:  # если закончилось место на диске
    S += Files[i - 1] + Files[i - 2]  # возвращаем файл, который не влез, и последний файл перед ним
    count -= 1
    i -= 1
    while i < len(Files) and S >= Files[i]:  # пока последний файл помещается в оставшееся место
        i += 1
    max_file = Files[i - 1]
    print(count, max_file)

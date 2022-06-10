with open("D:\\ЕГЭ\\ЕГЭ-22\\Статград 08.02.22\\27-B.txt", "r") as f:
    N = int(f.readline())
    count = 0
    count_d999 = [0] * 999  # список с количеством остатков от деления на 999
    S = 0
    for i in range(N):
        x = int(f.readline())
        S += x
        count += count_d999[S % 999]  # остатки от деления на 999 у текущей суммы и у предыдущих должны совпадать
        count_d999[S % 999] += 1
print(count)

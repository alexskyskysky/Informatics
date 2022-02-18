# Вариант 1 (2021)
with open("D:\\ЕГЭ\\ЕГЭ-21\\27\\27v01_B.txt", "r") as f:
    N = int(f.readline())
    max_sum = 0  # сумма максимальных чисел из каждой пары
    min_diff_nd31 = 100000  # минимальная разность чисел пары, которая не делится на 31
    for i in range(N):
        a, b = map(int, f.readline().split())
        max_sum += max(a, b)
        # если разность не делится на 31 и меньше текущей минимальной
        if abs(a - b) % 31 != 0 and abs(a - b) < min_diff_nd31:
            min_diff_nd31 = abs(a - b)
if max_sum % 31 == 0:  # если сумма делится на 31, нужно вычесть минимальную сумму, которая не делится на 31
    max_sum -= min_diff_nd31
print(max_sum)

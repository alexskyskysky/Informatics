with open("D:\\Downloads\\ЕГЭ-22\\Статград 17.21.21\\27-B.txt", "r") as f:
    N = int(f.readline())
    max_s = 0
    s = 0
    min_s30 = [10 ** 10] * 30
    # минимальные суммы с разными отстатками от деления k на 30
    k = 0
    for i in range(N):
        x = int(f.readline())
        s += x
        if x > 0 and x % 2 == 0:
            k += 1
        if k % 30 == 0 and s > max_s:
            max_s = s
        if min_s30[k % 30] != 10 ** 10:
            s_k = s - min_s30[k % 30]
            if s_k > max_s:
                max_s = s_k
        min_s30[k % 30] = min(s, min_s30[k % 30])
print(max_s)

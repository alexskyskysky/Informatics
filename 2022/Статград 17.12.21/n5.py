def SumEven(N):  # сумма чётных цифр числа
    S = 0
    while N > 0:
        if (N % 10) % 2 == 0:
            S += N % 10
        N //= 10
    return S


def SumOnEven(N):  # сумма цифр на чётных местах
    n = str(N)
    S = 0
    for i in range(
        1, len(n), 2
    ):  # сумма только по нечётных номерам в строке (в человеческом понимании это как раз цифры на чётных местах)
        S += int(n[i])
    return S


def R(N):  # алгоритм из задания
    S1 = SumEven(N)
    S2 = SumOnEven(N)
    return abs(S1 - S2)


for N in range(1000):
    if R(N) == 9:
        print(N)
        break

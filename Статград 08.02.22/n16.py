bin_n = format(1000000000, "b")
print(bin_n)
from math import factorial


def C(k, n):  # функция для расчёта сочетаний
    return (factorial(n)) // (factorial(n - k) * factorial(k))


k = 2  # потому что F(n)=2 по заданию
n = len(bin_n)  # количество знаков в миллиарде в двоичной системе
print(C(k, n))

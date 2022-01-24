# Вариант 1 (2022)
from math import factorial

t = "ИДИЛЛИЯ"
A = set(t)
result = factorial(len(t))  # числитель формулы перестановки с повторением
for symbol in A:
    result //= factorial(t.count(symbol))  # делим на факториалы повторяющихся символов
print(result)

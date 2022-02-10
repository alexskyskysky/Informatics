# Вариант 16 (2021)
def f(a, n):
    if n < a or n == 35:
        return 0
    if n == a:
        return 1
    S = f(a, n - 1)
    if n % 3 == 0:
        S += f(a, n // 3)
    return S


result = f(1, 12) * f(12, 40)
print(result)

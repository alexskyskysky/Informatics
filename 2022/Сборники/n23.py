# Вариант 1 (2022)
def f(a, n):
    if n < a:
        return 0
    if n == a:
        return 1
    S = f(a, n - 1)
    if n % 2 == 0:
        S += f(a, n // 2)
    if n % 5 == 0:
        S += f(a, n // 5)
    return S


Result = f(1, 10) * f(10, 20) * f(20, 38)
print(Result)

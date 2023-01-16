def f(a, n):
    if n == a:
        return 1
    if n < a:
        return 0
    S = f(a, n - 1)
    if n % 3 == 0:
        S += f(a, n // 3)
    return S


result = f(1, 11) * f(11, 34)
print(result)

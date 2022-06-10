def f(a, n, move):
    if n < a:
        return 0
    if n == a:
        return 1
    if move == 0:
        S = f(a, n - 1, 0) + f(a, n - 2, 0)
        if n % 2 == 0:
            S += f(a, n // 2, 1)
        return S
    if move == 1:
        return f(a, n - 1, 0) + f(a, n - 2, 0)


print(f(1, 11, 0))

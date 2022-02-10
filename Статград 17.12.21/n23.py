def f(n, a):
    if n > a:
        return 0
    if n == a:
        return 1
    return f(n + 1, a) + f(n + 2, a) + f(n * 3, a)


result = f(1, 8) * f(8, 15)
print(result)

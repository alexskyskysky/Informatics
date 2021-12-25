def f(a,n):
    if n<a:
        return 0
    if n==a:
        return 1
    S = f(a,n-1) + f(a,n-2)
    if n%3==0:
        S += f(a,n//3)
    return S

result = f(1,8)*f(8,15)
print(result)
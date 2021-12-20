#Вариант 1 (2021)
for ans in range(1000,1,-1):
    s = ans
    n = 1
    while s*n < 4096:
        s //= 2
        n *= 4
    if n==1024:
        print(ans)
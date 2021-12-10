#Вариант 1 (2021)
for ans in range(1000):
    x = ans
    Q = 15
    L = 0
    while x>=Q:
        L+=1
        x-=Q
    M = x
    if M<L:
        M=L
        L=x
    if L==3 and M==7:
        print(ans)
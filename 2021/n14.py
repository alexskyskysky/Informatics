#Вариант 1 (2021)
N = 5**2019 - 5**1019 + 25**600 - 125
result = 0
while (N>0):
    if N%5==4:
        result += 1
    N //= 5
print(result)

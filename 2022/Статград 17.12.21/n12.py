def F(t):
    while "1111" in t:
        t = t.replace("1111", "22", 1)
        t = t.replace("222", "1", 1)
    return t


max_Ones = 0  # максимальное число единиц
result_Length = 0  # минимальная длина для максимального числа единиц
for N in range(200, 300):
    t = "1" * N
    s = F(t)
    if s.count("1") > max_Ones:
        max_Ones = s.count("1")
        result_Length = N
print(result_Length)

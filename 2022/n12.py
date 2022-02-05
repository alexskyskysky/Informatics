# Вариант 1 (2022)
def F(t):
    while "02" in t or "04" in t or "06" in t:
        if "02" in t:
            t = t.replace("02", "6404", 1)
        if "04" in t:
            t = t.replace("04", "2206", 1)
        if "06" in t:
            t = t.replace("06", "440", 1)
    return t


N = 60
breaker = False
for a in range(1, N):
    for b in range(1, N):
        for c in range(1, N):
            t = "0" + "2" * a + "4" * b + "6" * c
            T = F(t)
            if T.count("2") == 30 and T.count("4") == 54 and T.count("6") == 10:
                print(c)
                breaker = True
                break
    if breaker:
        break

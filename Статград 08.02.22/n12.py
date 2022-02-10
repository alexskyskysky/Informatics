def F(t):
    while not ("00" in t):
        t = t.replace("01", "210", 1)
        t = t.replace("02", "3101", 1)
        t = t.replace("03", "2012", 1)
    return t


N = 80
Break = False
for a in range(N):
    for b in range(N):
        for c in range(N):
            t = "0" + "1" * a + "2" * b + "3" * c + "0"
            T = F(t)
            if T.count("1") == 70 and T.count("2") == 56 and T.count("3") == 24:
                print(a + b + c)
                Break = True
                break
        if Break:
            break
    if Break:
        break

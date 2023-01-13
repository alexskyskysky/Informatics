def R(N):
    n = format(N, "b")
    if N % 2 == 0:
        n += "01"
    else:
        n = "1" + n + "10"
    return int(n, 2)


for N in range(1000):
    if R(N) > 214:
        print(N)
        break

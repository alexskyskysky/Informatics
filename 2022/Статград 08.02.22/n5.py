def R(N):
    N_bin = format(N, "b")
    count0 = 0
    count1 = 0
    for k in range(len(N_bin)):
        if k % 2 == 0 and N_bin[k] == "0":
            count0 += 1
        elif k % 2 == 1 and N_bin[k] == "1":
            count1 += 1
    return abs(count1 - count0)


for N in range(2, 10000):
    if R(N) == 5:
        print(N)
        break

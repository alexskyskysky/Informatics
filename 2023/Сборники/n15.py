def Del(n, m):
    return n % m == 0


for A in range(1, 1000):
    count_x = 0
    for x in range(1, 1000):
        F = (Del(x, A) or (not Del(x, 27)) or (not Del(x, 89))) and (A > 300)
        if F == 1:
            count_x += 1
    if count_x == 999:
        print(A)
        break

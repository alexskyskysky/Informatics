def n2():
    print("x y z w F")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    F = (x and (not w)) or (y == z) or y
                    if F == 0:
                        print(x, y, z, w, F)


def R(N):
    b = format(N, "b")
    if N % 2 == 0:
        b = "10" + b
    else:
        b = "1" + b + "01"
    return int(b, 2)


def n5():
    for N in range(2, 1000):
        if R(N) > 441:
            print(N)
            break


def n6():
    for X in range(1000):
        s = X
        s = (s - 21) // 10
        n = 1
        while s > 0:
            n = n * 2
            s = s - n
        if n == 32:
            print(X)
            break


def n8():
    print(1 + int("01010", 5))


def n12():
    t = "8" * 84
    while "1111" in t or "8888" in t:
        if "1111" in t:
            t = t.replace("1111", "8", 1)
        else:
            t = t.replace("8888", "11", 1)
    print(t)


def n13():
    print("10")


def n14():
    N = 7 * 512 ** 1912 + 6 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022
    count = 0
    while N > 0:
        if N % 8 == 7:
            count += 1
        N //= 8
    print(count)


def Del(n, m):
    return n % m == 0


def n15():
    for A in range(1, 1000):
        count_F = 0
        for x in range(1, 1000):
            F = (not (Del(x, 3))) or (not (Del(x, 5))) or (x + A >= 90)
            if F:
                count_F += 1
        if count_F == 999:
            print(A)
            break


def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return F(n - 2) + F(n - 1) - n
    return F(n - 1) - F(n - 2) + 2 * n


def n16():
    print(F(32))


def n17():
    f = open("C:\\ЕГЭ\\ЕГЭ-22\\Варианты\\Открытый\\Файлы\\107_17.txt", "r")
    N = []
    for line in f:
        N.append(int(line))
    f.close()
    min_21 = 1000000
    count = 0
    max_sum = 0
    for i in range(len(N)):
        if N[i] % 21 == 0 and N[i] < min_21:
            min_21 = N[i]
    for i in range(1, len(N)):
        if N[i - 1] % min_21 == 0 or N[i] % min_21 == 0:
            count += 1
            if N[i - 1] + N[i] > max_sum:
                max_sum = N[i - 1] + N[i]
    print(count, max_sum)


def n18():
    print("2656 1665")


from functools import lru_cache


def Position(pos):
    n, s = pos
    return (n + 1, s), (n, s + 1), (n * 2, s), (n, s * 2)


@lru_cache(None)
def Game(pos):
    if sum(pos) >= 231:
        return "end"
    if any(Game(next_pos) == "end" for next_pos in Position(pos)):
        return "п1"
    if all(Game(next_pos) == "п1" for next_pos in Position(pos)):
        return "в1"
    if any(Game(next_pos) == "в1" for next_pos in Position(pos)):
        return "Петя-2"
    if all(Game(next_pos) == "п1" or Game(next_pos) == "Петя-2" for next_pos in Position(pos)):
        return "Ваня-2"
    return "#"


def n19_21():
    print("Задание 19: 54")
    print("Задание 20: 98 106")
    print("Задание 21: 97")


def n22():
    for n in range(10000, 1, -1):
        x = n
        Q = 8
        P = 10
        K1 = 0
        K2 = 0
        while x <= 100:
            K1 = K1 + 1
            x = x + P
        while x >= Q:
            K2 = K2 + 1
            x = x - Q
        L = x + K1
        M = x + K2
        if L == 12 and M == 19:
            print(n)
            break


def Q(a, n):
    if n < a:
        return 0
    if n == a:
        return 1
    S = Q(a, n - 2)
    if n % 2 == 0:
        S += Q(a, n // 2)
    return S


def n23():
    print(Q(1, 18) * Q(18, 52))


def n24():
    f = open("C:\\ЕГЭ\\ЕГЭ-22\\Варианты\\Открытый\\Файлы\\107_24.txt", "r")
    T = f.read().split("B")
    f.close()
    t_count = 0
    max_count = 0
    for i in range(len(T)):
        if T[i] == "A" or T[i] == "C":
            t_count += 1
        else:
            if t_count > max_count:
                max_count = t_count
            t_count = 0
    print(max(t_count, max_count))


def n25():
    for a in range(10):
        for b in range(10):
            N = int("12345" + str(a) + "7" + str(b) + "8")
            if N < 10 ** 9 and N % 23 == 0:
                print(N, N // 23)


def n26():
    f = open("C:\\ЕГЭ\\ЕГЭ-22\\Варианты\\Открытый\\Файлы\\107_26.txt", "r")
    N = int(f.readline())
    T = [[]]
    for _ in range(N):
        row, column = map(int, f.readline().split())
        T.append([row, column])
    f.close()
    T.sort(reverse=True)
    max_row = 0
    min_column = 10 ** 10
    for i in range(1, N):
        if T[i][0] == T[i - 1][0] and abs(T[i][1] - T[i - 1][1]) == 14:
            max_row = T[i][0]
            min_column = T[i][1] + 1
            break
    while T[i][0] == max_row:
        if abs(T[i][1] - T[i - 1][1]) == 14 and T[i][1] + 1 < min_column:
            min_column = T[i][1] + 1
        i += 1
    print(max_row, min_column)


def n27():
    f = open("C:\\ЕГЭ\\ЕГЭ-22\\Варианты\\Открытый\\Файлы\\107_27_A.txt", "r")
    N = int(f.readline())
    P = []
    for _ in range(N):
        P.append(int(f.readline()))
    f.close()
    R = []
    s = 0
    r = 0
    l = 0
    for i in range(1, N // 2):
        s += P[i] * i + P[N - i] * i
        r += P[i]
        l += P[N - i]
    R.append(s)
    for i in range(1, N):
        R.append(R[i - 1] - r + l + P[i - 1] - P[(i + N // 2 - 1) % N])
        r = r - P[i] + P[(i + N // 2 - 1) % N]
        l = l - P[(i + N // 2) % N] + P[i - 1]
    print(min(R))

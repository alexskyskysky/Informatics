def R(N):
    r = format(N, "b")
    if N % 2 == 0:
        r += "00"
    else:
        r += "10"
    if r.count("1") % 2 == 0:
        r += "0"
    else:
        r += "1"
    result = int(r, 2)
    return result


count = 0
for N in range(1, 1000):
    if 130 <= R(N) <= 350:
        count += 1
print(count)

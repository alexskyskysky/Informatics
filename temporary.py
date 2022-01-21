def R(N):
    B = format(N, "b")
    if N % 2 == 0:
        B += "00"
    else:
        B += "10"
    if B.count("1") % 2 == 0:
        B += "0"
    else:
        B += "1"
    return int(B, 2)


count = 0
for n in range(1, 10000):
    if 130 <= R(n) <= 350:
        count += 1
print(count)

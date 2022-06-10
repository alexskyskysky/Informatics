from math import sqrt, ceil


def M(N):
    L = ceil(sqrt(N))
    Div = []
    for d in range(2, L):
        if N % d == 0:
            Div.append(d)
            Div.append(N // d)
    if sqrt(N).is_integer():
        Div.append(sqrt(N))
    Div.sort(reverse=True)
    return Div[4] if len(Div) >= 5 else 0


n = 460000001
count = 0
while count < 5:
    m = M(n)
    if m > 0:
        count += 1
        print(m)
    n += 1

def toBin(dec): #перевод из десятичной в двоичную
    result = ''
    while(dec>0):
        result += str(dec%2)
        dec //= 2
    return result[::-1]

def toDec(bin): #перевод из двоичной в десятичную
    result = 0
    N = len(bin)
    for i in range(N):
        result += (2**(N-1-i)) * int(bin[i])
    return result 

def fromDectoN(N, Number): #перевод из десятичной системы в любую (с основанием N)
    result = ''
    while(Number>0):
        if Number%N<10:
            result += str(Number%N)
        else:
            result += chr(ord('A')+Number%N-10)
        Number //= N
    return result[::-1]


def fromNtoDec(N, Number): #перевод из любой системы (с основанием N) в десятичную
    result = 0
    L = len(Number)
    for i in range(L):
        if ord('A')<=ord(Number[i])<=ord('Z'):
            result += (N**(L-1-i)) * (10+ord(Number[i])-ord('A'))
        else:
            result += (N**(L-1-i)) * int(Number[i])
    return result 
import math

def isPrime(N): # проверка, является ли N простым
    if N==1:
        return False
    if N==2:
        return True
    L = math.ceil(math.sqrt(N))
    for k in range(2,L+1):
        if N%k==0:
            return False
    return True

def ToBin(N): # простой перевод в двоичную
    return format(N,'b')

def FromN_toDec(N, Number): # простой перевод из любой системы (с основанием N) в десятичную
    return int(Number,N)

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

def fromDec_toN(N, Number): #перевод из десятичной системы в любую (с основанием N)
    result = ''
    while(Number>0):
        if Number%N<10:
            result += str(Number%N)
        else:
            result += chr(ord('A')+Number%N-10)
        Number //= N
    return result[::-1]


def fromN_toDec(N, Number): #перевод из любой системы (с основанием N) в десятичную
    result = 0
    L = len(Number)
    for i in range(L):
        if ord('A')<=ord(Number[i])<=ord('Z'):
            result += (N**(L-1-i)) * (10+ord(Number[i])-ord('A'))
        else:
            result += (N**(L-1-i)) * int(Number[i])
    return result 

#примеры использования
print('Из 10-й в 2-ую:', toBin(25))
print('Из 2-й в 10-ую:', toDec('1100111'))
print('Из 10-й в 13-ую:', fromDec_toN(13,150))
print('Из 16-й в 10-ую:', fromN_toDec(16,'F4'))


#Вариант 1 (2021)
def toBin(dec):
    result = ''
    while(dec>0):
        result += str(dec%2)
        dec //= 2
    return result[::-1]

def toDec(bin):
    result = 0
    N = len(bin)
    for i in range(N):
        result += (2**(N-1-i)) * int(bin[i])
    return result 

def R(N):
    N -= N%4
    n = toBin(N)
    n += str(n.count('1')%2)
    n += str(n.count('1')%2)
    return toDec(n)

for N in range(1,56):
    if (R(N)>56):
        print(R(N))
        break

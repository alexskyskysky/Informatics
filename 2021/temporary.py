#Временный файл (код во время занятия; всегда разный)
def toBin(N):
    result = ''
    while(N>0):
        result += str(N%2)
        N //= 2
    return result[::-1]

def toDec(N):
    result = 0
    L = len(N)
    for i in range(L):
        result += (2**(L-1-i)) * int(N[i])
    return result

def R(N):
    N -= N%4
    b = toBin(N)
    b += str(b.count('1')%2)
    b += str(b.count('1')%2)
    return toDec(b)

for N in range(1,56):
    if (R(N)>56):
        print(R(N))

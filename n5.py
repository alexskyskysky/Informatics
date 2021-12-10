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

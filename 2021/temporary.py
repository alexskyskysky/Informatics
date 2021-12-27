#Временный файл (код во время занятия; всегда разный)
import math
def isPrime(N):
    if N==1:
        return False
    if N==2:
        return True
    L = math.ceil(math.sqrt(N))
    for k in range(2,L+1):
        if N%k==0:
            return False
    return True

for n in range(2,101):
    if isPrime(n):
        print(n)
        

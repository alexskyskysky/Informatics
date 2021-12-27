import math
def F(N):
    L = math.ceil(math.sqrt(N)) # последнее число в диапазоне проверки
    for k in range(2,L+1):
        if N%k==0:
            return N//k - k
    return 0

count = 0
N = 850001
while count<6:
    f = F(N)
    if f!=0 and f%7==0:
        count+=1
        print(N)
    N+=1
import math
def M(N):
    m = 0
    count = 0
    for k in range(2,math.ceil(math.sqrt(N))+1):
        if N%k==0:
            count += 1
            m += N//k
            if count==2:
                break
    if count==1:
        return m+1
    if count==2:
        return m
    return 0

result = 0
N=10000000
while result<5:
    if 0<M(N)<10000:
        result+=1
        print(N)
    N+=1
def Del(n,m):
    return n%m==0

n = 1000 #для диапазона x
for A in range(1,1000):
    count_F = 0
    for x in range(1,n):
        F = Del(x,A) or not(Del(x,18)) or not(Del(x,81))
        if F:
            count_F += 1
    if count_F == n-1:
        print(A)

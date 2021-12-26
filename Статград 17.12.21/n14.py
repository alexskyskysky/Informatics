N = 3*(125**6) + 2*(25**9) + + 5**12 - 625
count = 0
while N>0:
    if N%5 == 0:
        count+=1
    N //= 5
print(count)
k = 107
f = open("C:\\ЕГЭ\\ЕГЭ-23\\Сборник 14 вариантов\\Вариант 1\\Задание 27\\27-B.txt", "r")
n = int(f.readline())
S = 0
MaxS = []
MinL = []
MinS_D = [10**10] * k
MinS_i = [0] * k
for i in range(n):
    S += int(f.readline())
    if S % k == 0:
        MaxS.append(S)
        MinL.append(i + 1)
    elif MinS_D[S % k] != 10**10:
        MaxS.append(S - MinS_D[S % k])
        MinL.append(i - MinS_i[S % k])
    if S < MinS_D[S % k]:
        MinS_D[S % k] = S
        MinS_i[S % k] = i
f.close()

max_sum = max(MaxS)
min_len = 10**10
for i in range(len(MaxS)):
    if MaxS[i] == max_sum and MinL[i] < min_len:
        min_len = MinL[i]
print(min_len)

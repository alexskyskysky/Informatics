f = open('C:\\ЕГЭ-22\\Статград 17.12.21\\17.txt','r')
Numbers = list(map(int, f.readlines()))
f.close()

sum_even = 0 # сумма чётных
count_even = 0 # количество чётных
for i in range(len(Numbers)):
    if Numbers[i]%2==0:
        sum_even += Numbers[i]
        count_even += 1
avg_even = sum_even / count_even # среднее арифметическое чётных

count = 0 # количество подходящих пар
max_sum = -1 # максимальная сумма среди таких пар
for i in range(1,len(Numbers)):
    a = Numbers[i]
    b = Numbers[i-1]
    if (a%3==0 or b%3==0) and (a<avg_even or b<avg_even):
        count += 1
        if a+b > max_sum:
            max_sum = a+b
print(count, max_sum)

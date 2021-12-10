#Вариант 1
f = open('C:\\ЕГЭ-21\\24\\24 варианты 1-5.txt','r')
t = f.read()
f.close()

max_count = 0
t_count = 1
N = len(t)
for i in range(1,N):
    if ord(t[i])>=ord(t[i-1]):
        t_count += 1
    else:
        if t_count > max_count:
            max_count = t_count
        t_count = 1
print(max_count)
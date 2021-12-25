f = open('C:\\ЕГЭ-22\\Статград 17.12.21\\24.txt','r')
T = f.read()
f.close()

max_count = 0
t_count = 0
count_E = 0
for i in range(len(T)):
    if T[i]!='A':
        t_count += 1
        if T[i]=='E':
            count_E += 1
    else:
        if t_count > max_count and count_E >= 3:
            max_count = t_count
        t_count = 0
        count_E = 0
print(max_count)
        
    
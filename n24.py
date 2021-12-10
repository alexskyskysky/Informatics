f = open('C:\\ЕГЭ-21\\24\\24 варианты 1-5.txt','r')
t = f.read()
f.close()

max_count = 0
t_count = 0
N = len(t)
for i in range(N):
    if t[i]!='Z':
        t_count += 1
    else:
        if t_count > max_count:
            max_count = t_count
        t_count = 0
print(max_count)
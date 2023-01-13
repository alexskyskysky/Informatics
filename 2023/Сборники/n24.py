f = open("C:\\ЕГЭ\\ЕГЭ-23\\Сборник 14 вариантов\\Вариант 2\\Задание 24\\24-var2.txt")
t = f.read()
f.close()

G = "EI"
S = "FGH"
max_count = -1
t_count = 0
for i in range(1,len(t),2):
    if (t[i-1] in G and t[i] in G) or (t[i-1] in S and t[i] in S):
        t_count += 1
    else:
        if t_count > max_count:
            max_count = t_count
        t_count = 0
if t_count > max_count:
    max_count = t_count
print(max_count)
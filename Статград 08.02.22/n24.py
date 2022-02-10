f = open("D:\\ЕГЭ\\ЕГЭ-22\\Статград 08.02.22\\24.txt", "r")
t = f.read()
f.close()

count = 0
t_count = 2
contains_F = True
for i in range(len(t)):
    if t[i] == "E":
        if t_count >= 12 and not contains_F:
            count += 1
        t_count = 2
        contains_F = False
    else:
        t_count += 1
        if t[i] == "F":
            contains_F = True
print(count)

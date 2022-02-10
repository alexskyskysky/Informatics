# Вариант 10 (2021 - Сборник 10 вариантов)
f = open("C:\\ЕГЭ-21\\Сборник 10 вариантов\\Вариант 10\\24\\24.txt", "r")
t = f.read()
f.close()

max_count = 0
t_count = 0
i = 2
while i < len(t):
    if t[i - 2] == "?" and t[i - 1] == "!" and t[i] == "?":
        t_count += 3
        i += 3
    else:
        if t[i - 2] == "?":
            t_count += 1
            if t[i - 1] == "!":
                t_count += 1
        if t_count > max_count:
            max_count = t_count
        t_count = 0
        i += 1
print(max(max_count, t_count))

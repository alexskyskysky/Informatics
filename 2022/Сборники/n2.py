# Вариант 1 (2022)
print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x) or y) and (x == (not z)) and w
                if F:
                    print(x, y, z, w, F)

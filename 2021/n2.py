# Вариант 1 (2021)
print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = not (not (x) or y) or not (z) or w
                if F == 0:
                    print(x, y, z, w, F)

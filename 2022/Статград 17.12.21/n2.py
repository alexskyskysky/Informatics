print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = not ((not (x) or y) and (z or w)) or ((x == w) or (y and not (z)))
                if F == 0:
                    print(x, y, z, w, F)

N = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C"]
n1 = "186x4"
n2 = "5x716"

for d in N:
    x1 = int(n1.replace("x", d), 13)
    x2 = int(n2.replace("x", d), 13)
    if (x1 + x2) % 11 == 0:
        print((x1 + x2) // 11)

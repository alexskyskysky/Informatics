f = open("D:\\ЕГЭ\\ЕГЭ-22\\Статград 08.02.22\\26.txt", "r")
N = int(f.readline())
P = []
for i in range(N):
    row, column = map(int, f.readline().split())
    P.append([row, column])
f.close()

P.sort()
max_count = 0
row_number = -1
count = 1
for i in range(1, N):
    if P[i] == P[i - 1]:
        continue
    if P[i][0] == P[i - 1][0] and P[i][1] - P[i - 1][1] == 1:
        count += 1
    else:
        if count > max_count:
            max_count = count
            row_number = P[i - 1][0]
        count = 1
print(max(max_count, count), row_number)

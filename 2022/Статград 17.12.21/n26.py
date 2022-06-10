week = 7 * 24 * 60 * 60
P = [0] * (week + 1)
start = 1633305600
end = start + week

processes = 0

with open("D:\\Downloads\\ЕГЭ-22\\Статград 17.21.21\\26.txt", "r") as f:
    N = int(f.readline())
    for i in range(N):
        p_start, p_end = map(int, f.readline().split())
        if p_start < start and (p_end > end or end == 0):
            processes += 1
        if start <= p_start <= end:
            P[p_start - start] += 1
        if start <= p_end <= end:
            P[p_end - start] -= 1

max_processes = 0
max_time = 0
for i in range(len(P)):
    processes += P[i]
    if processes > max_processes:
        max_processes = processes
        max_time = 0
    if processes == max_processes:
        max_time += 1
max_time -= 1
print(max_processes, max_time)

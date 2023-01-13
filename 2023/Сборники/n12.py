t = ">" + "2" * 15 + "3" * 20 + "5" * 25
while ">2" in t or ">3" in t or ">5" in t:
    if ">2" in t:
        t = t.replace(">2", "333>", 1)
    if ">3" in t:
        t = t.replace(">3", "23>", 1)
    if ">5" in t:
        t = t.replace(">5", "35>", 1)
S = 0
for i in range(len(t) - 1):
    S += int(t[i])
print(S)

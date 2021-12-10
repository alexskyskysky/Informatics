#Вариант 15 (2021)
t = 'AB123'
result = 0
for a in range(len(t)):
    for b in range(len(t)):
        for c in range(len(t)):
            for d in range(len(t)):
                s = t[a]+t[b]+t[c]+t[d]
                if s.count('A')+s.count('B')==1:
                    result += 1
print(result)
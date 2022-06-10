t = "СВЕТЛАНА"
count = 0
Words = set()
for a in range(len(t)):
    for b in range(len(t)):
        for c in range(len(t)):
            for d in range(len(t)):
                for e in range(len(t)):
                    for f in range(len(t)):
                        for g in range(len(t)):
                            for h in range(len(t)):
                                s = t[a] + t[b] + t[c] + t[d] + t[e] + t[f] + t[g] + t[h]
                                if (
                                    s.count("А") == 2
                                    and len(set(s)) == 7
                                    and s[0] != s[1]
                                    and s[1] != s[2]
                                    and s[2] != s[3]
                                    and s[3] != s[4]
                                    and s[4] != s[5]
                                    and s[5] != s[6]
                                    and s[6] != s[7]
                                ):
                                    Words.add(s)
print(len(Words))

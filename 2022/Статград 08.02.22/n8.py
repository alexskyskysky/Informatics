def isCorrectWord(word):
    return (
        word.count("Р") == 1
        and word.count("С") == 1
        and word.count("М") == 1
        and word.count("Х") == 1
        and word.count("О") == 2
        and word.count("А") == 2
    )


Words = set()
S = "РСМХ"
G = "ОА"
for g1 in G:
    for s1 in S:
        for g2 in G:
            for s2 in S:
                for g3 in G:
                    for s3 in S:
                        for g4 in G:
                            for s4 in S:
                                word1 = g1 + s1 + g2 + s2 + g3 + s3 + g4 + s4
                                word2 = s1 + g1 + s2 + g2 + s3 + g3 + s4 + g4
                                if isCorrectWord(word1):
                                    Words.add(word1)
                                if isCorrectWord(word2):
                                    Words.add(word2)
print(len(Words))

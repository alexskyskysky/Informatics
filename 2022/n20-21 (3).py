# Вариант 7 (2022)
from functools import lru_cache


def Position(pos):
    a, s = pos
    M = []
    if a < 270:  # (808-1)/3, т.к. 1 - минимальное значение S
        M.append((a + 2, s))
    if s < 258:  # (808-35)/3, т.к. 35 - минимальное значение a
        M.append((a, s + 2))
    M.append((a * 3, s))
    M.append((a, s * 3))
    return M


@lru_cache(None)
def Game(pos):
    if pos[0] + pos[1] >= 808:
        return "end"
    if any(Game(next_pos) == "end" for next_pos in Position(pos)):
        return "к1"
    if all(Game(next_pos) == "к1" for next_pos in Position(pos)):
        return "с1"
    if any(Game(next_pos) == "с1" for next_pos in Position(pos)):
        return "Коля-2"
    if all(Game(next_pos) == "к1" or Game(next_pos) == "Коля-2" for next_pos in Position(pos)):
        return "Саша-2"
    return "#"


for S in range(50, 300):
    pos = 35, S
    print(S, Game(pos))

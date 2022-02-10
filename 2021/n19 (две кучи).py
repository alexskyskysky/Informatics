# Вариант 1 (2021)
from functools import lru_cache


def Position(pos):
    a, S = pos
    return (a + 2, S), (a, S + 2), (a * 2, S), (a, S * 2)


@lru_cache(None)
def Game(pos):
    if pos[0] + pos[1] >= 142:
        return "end"
    if any(Game(next_pos) == "end" for next_pos in Position(pos)):
        return "п1"
    if any(Game(next_pos) == "п1" for next_pos in Position(pos)):
        return "Ваня-1"
    return "#"


for S in range(1, 138):
    p = 2, S
    print(S, Game(p))

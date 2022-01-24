# Вариант 1 (2022)
from functools import lru_cache


def Position(S):
    return S + 1, S + 3, S * 4


@lru_cache(None)
def Game(S):
    if S >= 78:
        return "end"
    if any(Game(next_S) == "end" for next_S in Position(S)):
        return "п1"
    if any(Game(next_S) == "п1" for next_S in Position(S)):
        return "Ваня-1"
    return "#"


for S in range(1, 78):
    print(S, Game(S))

# Вариант 16 (2021)
from functools import lru_cache


def Position(pos):
    a, s = pos
    return (a + 6, s), (a, s + 6), (a ** 2, s), (a, s ** 2)


@lru_cache(None)
def Game(pos):
    if sum(pos) >= 200:
        return "end"
    if any(Game(next_p) == "end" for next_p in Position(pos)):
        return "п1"
    if all(Game(next_p) == "п1" for next_p in Position(pos)):
        return "в1"
    if any(Game(next_p) == "в1" for next_p in Position(pos)):
        return "Петя-2"
    # ниже два if, т.к. в задании просят, чтобы Ваня обязательно имел шанс победить в один ход
    if all(
        Game(next_p) == "Петя-2" or Game(next_p) == "п1" for next_p in Position(pos)
    ):
        if any(Game(next_p) == "п1" for next_p in Position(pos)):
            return "Ваня-2"
    return "#"


for S in range(2, 100):  # перебор от 2, чтобы 1 вечно не возводилось в квадрат
    start_pos = 3, S
    print(S, Game(start_pos))

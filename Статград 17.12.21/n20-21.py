from functools import lru_cache


def Position(pos):  # S - куча камней, move - последний ход
    # move=0 - начало игры, move=1 - до этого было +1, move=2 - до этого было +2, move=3 - до этого было *2
    S, move = pos
    if move == 0:
        return (S + 1, 1), (S + 2, 2), (S * 2, 3)
    if move == 1:
        return (S + 2, 2), (S * 2, 3)
    if move == 2:
        return (S + 1, 1), (S * 2, 3)
    if move == 3:
        return (S + 1, 1), (S + 2, 2)


@lru_cache(None)
def Game(Pos):
    S, move = Pos
    if S >= 34:
        return "end"
    if any(Game(next_pos) == "end" for next_pos in Position(Pos)):
        return "п1"
    if all(Game(next_pos) == "п1" for next_pos in Position(Pos)):
        return "в1"
    if any(Game(next_pos) == "в1" for next_pos in Position(Pos)):
        return "Петя-2"
    if all(
        Game(next_pos) == "Петя-2" or Game(next_pos) == "п1"
        for next_pos in Position(Pos)
    ):
        return "Ваня-2"
    return "#"


for S in range(1, 33):
    pos = S, 0
    print(S, Game(pos))

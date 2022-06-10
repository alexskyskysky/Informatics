from functools import lru_cache


def NewLastMoves(OldLastMoves, current_player, current_move):
    another_player = 1 if current_player == 0 else 0
    New = [0, 0]
    New[current_player] = current_move
    New[another_player] = OldLastMoves[another_player]
    return tuple(New)


def Position(pos):  # S - куча камней,
    # LastMoves - список из двух элементов с последним ходом каждого из игроков,
    # current_player - текущий игрок (=0 для Пети, =1 для Вани),
    # Moves[]=0 - начало игры, =1 - до этого было +1, =2 - до этого было +2, =3 - до этого было *2
    S, LastMoves, current_player = pos
    another_player = 1 if current_player == 0 else 0

    if LastMoves[current_player] == 0:
        return (
            (S + 1, NewLastMoves(LastMoves, current_player, 1), another_player),
            (S + 2, NewLastMoves(LastMoves, current_player, 2), another_player),
            (S * 2, NewLastMoves(LastMoves, current_player, 3), another_player),
        )
    if LastMoves[current_player] == 1:
        return (
            (S + 2, NewLastMoves(LastMoves, current_player, 2), another_player),
            (S * 2, NewLastMoves(LastMoves, current_player, 3), another_player),
        )
    if LastMoves[current_player] == 2:
        return (
            (S + 1, NewLastMoves(LastMoves, current_player, 1), another_player),
            (S * 2, NewLastMoves(LastMoves, current_player, 3), another_player),
        )
    if LastMoves[current_player] == 3:
        return (
            (S + 1, NewLastMoves(LastMoves, current_player, 1), another_player),
            (S + 2, NewLastMoves(LastMoves, current_player, 2), another_player),
        )


@lru_cache(None)
def Game(pos):
    S = pos[0]
    if S >= 21:
        return "end"
    if any(Game(next_pos) == "end" for next_pos in Position(pos)):
        return "п1"
    if all(Game(next_pos) == "п1" for next_pos in Position(pos)):
        return "в1"
    if any(Game(next_pos) == "в1" for next_pos in Position(pos)):
        return "Петя-2"
    if all(Game(next_pos) == "п1" or Game(next_pos) == "Петя-2" for next_pos in Position(pos)):
        return "Ваня-2"
    if any(Game(next_pos) == "в1" or Game(next_pos) == "Ваня-2" for next_pos in Position(pos)):
        return "Петя-3"
    return "#"


for S in range(1, 21):
    pos = (S, (0, 0), 0)
    print(S, Game(pos))

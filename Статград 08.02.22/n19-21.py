from functools import lru_cache


def NewMoves(Moves, player, move):
    another_player = 1 if player == 0 else 0
    New = [0, 0]
    New[player] = move
    New[another_player] = Moves[another_player]
    return tuple(New)


def Position(pos):  # S - куча камней, move - последний ход
    # Moves - список из двух элементов с последним ходом каждого из игроков
    # player=0 для Пети, player=1 для Вани
    # move=0 - начало игры, move=1 - до этого было +1, move=2 - до этого было +2, move=3 - до этого было *2
    S, Moves, player = pos
    another_player = 1 if player == 0 else 0

    if Moves[player] == 0:
        return (
            (S + 1, NewMoves(Moves, player, 1), another_player),
            (S + 2, NewMoves(Moves, player, 2), another_player),
            (S * 2, NewMoves(Moves, player, 3), another_player),
        )
    if Moves[player] == 1:
        return (S + 2, NewMoves(Moves, player, 2), another_player), (S * 2, NewMoves(Moves, player, 3), another_player)
    if Moves[player] == 2:
        return (S + 1, NewMoves(Moves, player, 1), another_player), (S * 2, NewMoves(Moves, player, 3), another_player)
    if Moves[player] == 3:
        return (S + 1, NewMoves(Moves, player, 1), another_player), (S + 2, NewMoves(Moves, player, 2), another_player)


@lru_cache(None)
def Game(pos):
    S, Moves, player = pos
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

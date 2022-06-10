# Вариант 5 (2022)
from functools import lru_cache


def Position(pos):
    N, K = pos
    M = []
    if N >= 3 and K >= 3:
        M.append((N - 3, K - 3))
    if N % 2 == 0 and N > 0:
        M.append((N // 2, N // 2))
    if K % 2 == 0 and K > 0:
        M.append((K // 2, K // 2))
    return M


@lru_cache(None)
def Game(pos):
    N, K = pos
    if (N < 2 and K % 2 != 0) or (K < 2 and N % 2 != 0) or (N < 2 and K < 2):
        return "end"
    if any(Game(next_pos) == "end" for next_pos in Position(pos)):
        return "с1"
    if all(Game(next_pos) == "с1" for next_pos in Position(pos)):
        return "а1"
    if any(Game(next_pos) == "а1" for next_pos in Position(pos)):
        return "Сергей-2"
    if all(Game(next_pos) == "Сергей-2" or Game(next_pos) == "с1" for next_pos in Position(pos)):
        return "Анатолий-2"
    return "#"


N = 32
for K in range(2, 70):
    pos = N, K
    print(K, Game(pos))

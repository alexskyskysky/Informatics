from functools import lru_cache


def Position(S):
    return S + 1, 4 * S - 3


@lru_cache(None)
def Game(S):
    if S >= 136:
        return "end"
    if any(Game(next_S) == "end" for next_S in Position(S)):
        return "п1"
    if all(Game(next_S) == "п1" for next_S in Position(S)):
        return "в1"
    return "#"


for S in range(2, 130):
    print(S, Game(S))

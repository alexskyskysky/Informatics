from functools import lru_cache
def Position(pos): # S - куча камней, move - последний ход
    S,move = pos
    if move == 0:
        return (S+1,1),(S+2,2),(S*2,3)
    if move == 1:
        return (S+2,2),(S*2,3)
    if move == 2:
        return (S+1,1),(S*2,3)
    if move == 3:
        return (S+1,1),(S+2,2)
@lru_cache(None)
def Game(Pos):
    S,move = Pos
    if S>=34:
        return 'end' 
    if any(Game(next_pos)=='end' for next_pos in Position(Pos)):
        return 'п1'
# all, потому что по-другому сформулировано задание №19. спрашивают ДЛЯ ВСЕХ ходов Пети
    if all(Game(next_pos)=='п1' for next_pos in Position(Pos)):
        return 'Ваня-1'

for S in range(1,33):
    pos = S,0
    print(S, Game(pos))
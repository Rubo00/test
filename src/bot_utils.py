from field_utils import COMBINATIONS
from random import choice


def bot_turn(field: list[list[str]]) -> None:
    groups: list[tuple[int, int, int, list[tuple[int, int]]]] = []
    for comb in COMBINATIONS:
        spaces = 0
        x_count = 0
        o_count = 0
        blank_cells = []
        for ridx, cidx in comb:
            cell = field[ridx][cidx]
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1
            else:
                spaces += 1
                blank_cells.append((ridx, cidx))
        groups.append((spaces, x_count, o_count, blank_cells))
    pri1 = []
    pri2 = []
    pri3 = []
    for group in groups:
        s, x, o, _ = group
        if o == 2 and s == 1:
            pri1.append(group)
        elif x == 2 and s == 1:
            pri2.append(group)
        elif s > 0:
            pri3.append(group)
    for pri in [pri1, pri2, pri3]:
        if pri:
            _, _, _, cells = choice(pri)
            ridx, cidx = choice(cells)
            field[ridx][cidx] = "O"
            return
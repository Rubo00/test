COMBINATIONS = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
]

LETTER_MAP = {"A": 0,"B":1 , "C":2}
NUMBER_MAP = {"1": 0 ,"2": 1, "3": 2}

def check_winner(field: list[list[str]]) -> str | None:
    empty_space = False 
    for comb in COMBINATIONS:
        x_count = 0 
        o_count = 0
        for ridx,cidx in comb:
            value = field[ridx][cidx]
            if value == " ":
                empty_space = True
            elif value == "X":
                x_count += 1
            else:
                o_count += 1 
        if x_count ==3:
            return "X"
        elif o_count == 3:
            return "O"
    if empty_space:
        return
    else:
        return " " 
    

def generate_field(): 
    field = [
        [" ", " ", " " ],
        [" ", " ", " " ],    
        [" ", " ", " " ],
    ]

    return field


def tranform_coord_to_index(coords: tuple[str,str]):
    lcoord, ncoord = coords
    return LETTER_MAP[lcoord],NUMBER_MAP[ncoord]

def write_cell(field: list[list[str]], idx: tuple[str,int])-> bool:
    ridx , cidx = idx
    if field[ridx][cidx]== " ":
        field [ridx][cidx] = "X"
        return True
    return False

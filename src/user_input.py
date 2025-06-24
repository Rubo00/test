from field_utils import write_cell, tranform_coord_to_index

VALID_LETTERS = {"A","B","C"} 
VALID_NUMBERS = { "1", "2", "3"}

def user_turn(field: list[list[str]]):
    while True:
        coord = get_user_coordinates_input()
        idx = tranform_coord_to_index(coord)
        if write_cell(field, idx):
            break
        print("Ячейка занята")

def get_user_coordinates_input():
     while True:
        user_input = input(": ").upper().strip()
        if len(user_input) != 2:
            print("Неверный ввод")
            continue
        lcoord, ncoord = user_input
        if lcoord not in VALID_LETTERS or ncoord not in VALID_NUMBERS:
            print("Неверный ввод")
            continue
        return lcoord, ncoord
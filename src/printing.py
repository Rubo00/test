HELLO_TEXT = "Привет!\nЭто крестики нолики!"
NUM_COORDS = "    1   2   3  \n"
LETTER_COORDS = ("A", "B", "C")
SPLIT_LINE = "  -------------\n"


def print_hello() -> None:
    print(HELLO_TEXT)

def print_winner(symbol: str) -> None:
    if symbol == " ":
        print("Победила дружба!")
    elif symbol == "X":
        print("Вы победили!")
    else:
        print("Победил бот!")

def print_field(field: list[list[str]]) -> None:
    field_str = SPLIT_LINE
    for row in field:
        field_str += "| "
    field_str = NUM_COORDS + SPLIT_LINE
    for row, letter in zip(field, LETTER_COORDS):
        field_str += letter + " | "
        for item in row:
            field_str += item + " | "
        field_str += "\n" + SPLIT_LINE
    print(field_str)
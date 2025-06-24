from bot_utils import bot_turn
from field_utils import generate_field, check_winner
from printing import print_field, print_hello, print_winner
from user_input import user_turn

def check_end_game(field) -> None:
    winner = check_winner(field)
    if winner:
        print_field(field)
        print_winner(winner)
        exit(0)
 
def main():
    print_hello()
    field = generate_field()
    while True:
        print_field(field)
        user_turn(field)
        check_end_game(field)
        bot_turn(field)
        check_end_game(field)


if __name__ == "__main__":
    main()
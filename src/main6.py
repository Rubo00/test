from database import Database
from settings import DB_PATH

MENU = """1. ---
0. Выход"""
MENU_CHOICES = {0, 1}


def get_user_choice() -> int:
    while True:
        try:
            user_input = int(input().strip())
            if user_input not in MENU_CHOICES:
                raise ValueError
        except ValueError:
            print("Это не пункт меню! Попробуйте еще раз.")
        else:
            return user_input


def main():
    print("Привет! Это программа для помощи учета товара на складе")
    database = Database(DB_PATH)
    database.create_tables()
    while True:
        print(MENU)
        user_input = get_user_choice()
        if user_input == 0:
            break
    print("Завершение работы программы...")


if __name__ == "__main__":
    main()
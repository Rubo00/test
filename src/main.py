from get_names import read_names
from get_initials import format_names
from config import READ_PATH, WRITE_PATH
import config
def main():
    names = read_names(READ_PATH)
    formated_names=format_names(names)
    print(formated_names)

main()
import json
from datetime import datetime

def get_questions(path: str = "questions.json") -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_table(path: str = "results.json") -> list[dict[str, str | int]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)



def write_table(table: list[dict[str, str | int]], path: str = "results.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        return json.dump(table, f, ensure_ascii=False, indent=4)


def main():
    user_name = input("Ваше имя: ")
    start = datetime.now()
    questions = get_questions()
    points = 0
    for q in questions:
        print(q["question"])
        user_input = input(": ")
        if user_input.strip() == q["answer"]:
            points += 1
    end = datetime.now()
    time = int((end - start).total_seconds())
    print(f"Вы набрали {points} баллов за {time} с")
    table = get_table()
    table.append({"name": user_name, "points": points, "seconds": time})
    write_table(table)


if __name__ == "__main__":
    main()
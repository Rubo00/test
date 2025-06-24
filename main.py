"""class User:
    def __init__(self, name:str , age:int) : 
        self.name = name
        self.age = age
    def hello(self):
        print(f"Привет ,я {self.name}, мне {self.age}")
sasha = User("sasha", 22)
petya = User("petya", 23)
sasha.hello()
petya.hello()"""

from datetime import datetime


class User:
    def __init__(self, name: str):
        self.name = name


class Question:
    def __init__(self, question: str, answer: str, difficulty: int):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def print(self):
        print(self.question)

    def check_answer(self, user_answer: str) -> bool:
        return self.answer.lower() == user_answer.lower()


class Game:
    def __init__(self, user: User, questions: list[Question]):
        self.score = 0
        self.user = user
        self.start_time = datetime.now()
        self.questions = questions
        self.index_of_questions = 0
        self.last_index = len(questions) - 1

    def print_question(self):
        self.current_question = self.questions[self.index_of_questions]
        self.current_question.print()

    def user_answer(self):
        user_input = input(": ")
        if self.current_question.check_answer(user_input):
            self.score += self.current_question.difficulty
            print("ОК")
        else:
            print("НЕ ОК")
        self.index_of_questions += 1

    def end(self):
        sec = (datetime.now() - self.start_time).total_seconds()
        print(f"Поздравляю {self.user.name}, вы завершили игру за {sec} и набрали {self.index_of_questions} баллов")   

def main():
    name = input("Имя: ")
    user = User(name)
    questions = [
        Question("Столица России?", "Москва", 1),
        Question("Столица Франции?", "Париж", 2),
    ]
    game = Game(user, questions)
    while game.index_of_questions <= game.last_index:
        game.print_question()
        game.user_answer()
    game.end()
   

main()
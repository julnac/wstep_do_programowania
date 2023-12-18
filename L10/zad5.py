import csv
import random


REWARDS = [500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]


class Question:

    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f'{chr(65 + i)}) {option}')


def add_question(file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        while True:
            question = input("Dodaj pytanie w formacie: pytanie,opcjaA,opcjaB,opcjaC,opcjaD,poprawna: ")
            if question == 'end':
                break
            file.write(question + '\n')


def load_questions(file_name):
    questions = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header if present
        for row in reader:
            question = Question(row[0], row[1:5], row[5])
            questions.append(question)
    return questions


def play_game(file_name):
    questions = load_questions(file_name)

    game_over = False
    counter = 0
    lifebuoys = 3

    while not game_over:
        print(f'---- Runda {counter + 1}, gramy o {REWARDS[counter]} zł ----')
        question = random.choice(questions)
        print(question.question)
        counter += 1
        for i, answer in enumerate(question.options):
            print(f'{chr(i + 65)}) {answer}')

        answer_received = False
        while not answer_received:
            answer = input(f"Podaj odpowiedź 'a,b,c,d',\nlub '0' po koło ratunkowe (dostępne {lifebuoys}): ")

            if answer == '0':
                if lifebuoys > 0:
                    print(f"Przyjaciel mówi że dobra odp to '{question.correct_answer}'.")
                    lifebuoys -= 1
                else:
                    print(f"Przyjacielu, nie masz już kół!")
            elif answer in ['a', 'b', 'c', 'd']:
                if answer == question.correct_answer:
                    print("Dobra odpowiedź, gramy dalej.")
                else:
                    print("Zła odpowiedź. Koniec Gry!")
                    game_over = True

                answer_received = True
            else:
                print(f"Przyjacielu, podaj odpowiedź z dostępnych: 'a,b,c,d'")

        questions.remove(question)
        if counter == len(REWARDS):
            print("Wygrałeś!")
            game_over = True


def process_question(line):
    return Question(line[0], line[1:5], line[-1])


def main():
    print("----STARTING MENU----")
    print("1. Add questions")
    print("2. PLAY")

    choice = input("Wybierz opcje: ")
    if choice == "1":
        add_question('questions.csv')
    elif choice == "2":
        play_game('questions.csv')


if __name__ == "__main__":
    main()
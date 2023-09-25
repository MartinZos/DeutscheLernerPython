import random

# List of sentences with answers and questions
sentences = [
    ("sam", "allein"),
    ("vynikajúci", "ausgezeichnet"),
    ("Bavorsko", "Bayern"),
    ("správa", "der Bericht"),
    ("zaoberať sa niečím", "beschäftigen sich mit etwas"),
    ("byť zaneprázdnený", "beschäftigt sein"),
    ("raz", "elnmal"),
    ("fantastický", "fantastisch"),
    ("prázdniny", "die Ferien"),
    ("Čo tam bolo vidieť?", "Was gab es zu sehen?"),
    ("celkom skvelý", "ganz toll"),
    ("celý deň", "den ganzen Tag"),
    ("proti", "gegen"),
    ("včera", "gestern"),
    ("nádherný", "herrlich"),
    ("prvotriedny, vynikajúci", "klasse"),
    ("variť", "kochen"),
    ("posledný", "der letzte"),
    ("majster", "der Meister"),
    ("Všetkému sa treba učit", "Übung macht den Meister"),
    ("hráč národného družstva", "der Nationalspieler"),
    ("organizovať", "organisieren"),
    ("prima, výborný", "prima"),
    ("dážď", "der Regen"),
    ("hra s pridelenými úlohami", "das Rollenspiel"),
    ("veta", "der Satz")
]

def quiz():
    score = 0
    total = len(sentences)
    random.shuffle(sentences)

    for word, translation in sentences:
        user_input = input(f"What is the translation of '{word}'? (Press 'q' to quit): ").strip()

        if user_input.lower() == translation.lower():
            print("True")
            score += 1
        else:
            print(f"False. The correct translation is '{translation}'.")

        if user_input.lower() == 'q':
            break

    print(f"You got {score} out of {total} correct.")


while True:
    print("Menu:")
    print("1. Start Quiz")
    print("2. Quit")

    choice = input("Enter your choice (1/2): ").strip()

    if choice == '1':
        quiz()
    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

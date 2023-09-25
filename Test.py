import random
import os

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
# List of sentences with answers and questions
sentences = [
    ("senzacny", "sensationell"),
    ("hladat", "suchen"),
    ("cast, diel", "der Teil"),
    ("nezdvorily", "unhoflich"),
    ("nejasny", "unklar"),
    ("nepresny", "unkorrekt"),
    ("nemoderny", "unmodern"),
    ("neprakticky", "unpraktisch"),
    ("podujatie", "die Veranstaltung"),
    ("zakaz", "das Verbot"),
    ("plny", "voll"),
    ("predtym", "vorher"),
    ("vpredu", "vorn"),
    ("navrh", "der Vorschlag"),
    ("prednaska", "der Vortrag"),
    ("pravda", "wahr"),
    ("dost, znacne", "ziemlich"),
    ("medzi", "zwischen"),
    ("metoda", "die Methode"),
    ("sused", "der Nachbar"),
    ("popoludnie", "der Nachmittag"),
    ("nutny", "notig"),
    ("organizacia", "die Organisation"),
    ("pefektny", "perfekt"),
    ("plan", "der Plan"),
    ("planovat", "planen"),
    ("planovanie", "die Planung"),
    ("premysleny, podla planu", "planvoll"),
    ("prezentacia", "die Prasentation"),
    ("presny na cas", "punktlich"),
    ("referent", "der Referent"),
    ("policka", "das Regal"),
    ("pravidlo", "die Regel"),
    ("kolo", "die Runde"),
    ("skoda", "schade"),
    ("znacka,tabulka stitok", "das Schild"),
    ("poznamkovy blok", "der Schreibblock"),
    ("podivny,cudny", "seltsam"),
    ("prijemny", "angenehm"),
    ("strom", "der Baum"),
    ("potom", "danach"),
    ("jednoduchy", "einfach"),
    ("zapisat", "eintragen"),
    ("priatelsky", "freundlich"),
    ("do pat", "zu funf"),
    ("myslienka", "der Gedanke"),
    ("presne", "genau"),
    ("nekompetentny", "inkompetent"),
    ("komplikovany", "kompliziert"),
    ("dlzka", "die Lange"),
    ("nudny", "langweilig"),
    ("ucebnica", "das Lehrwerk"),
    ("obsah", "der Inhalt"),
    ("lahky", "leicht"),
    ("vesely", "lustig"),
    ("mienka", "die Meinung"),
    ("sam", "allein"),
    ("vynikajuci", "ausgezeichnet"),
    ("raz", "einmal"),
    ("sprava", "der Bericht"),
    ("celkom", "ganz"),
    ("proti", "gegen"),
    ("vcera", "gestern"),
    ("predvcerom", "vorgestern"),
    ("nadherny", "herrlich"),
    ("prvotriedny", "klasse"),
    ("varit", "kochen"),
    ("posledny", "der Letzte"),
    ("majster", "der Meister"),
    ("Hrac narodneho druzstva", "der Nationalspieler"),
    ("organizovat", "organisieren"),
    ("oci", "der Papa"),
    ("prima", "prima"),
    ("dazd", "der Regen"),
    ("hra s pridelenymi ulohami", "das Rollenspiel"),
    ("veta", "der Satz"),
    ("plavat", "schwimmen"),
    ("vidiet", "sehen"),
    ("vyborny", "spitze"),
    ("zapcha", "der Stau"),
    ("cele hodiny", "stundenlang"),
    ("super", "super"),
    ("supermarket", "der Supermarkt"),
    ("tabulka", "die Tabelle"),
    ("bajecny", "toll"),
    ("turnaj", "das Turnier"),
    ("anketa", "die Umfrage"),
    ("dovolenka", "der Urlaub"),
    ("od do", "von bis"),
    ("bol", "war"),
    ("voda", "das Wasser"),
    ("pocasie", "das Wetter"),
    ("slovnik", "das Worterbuch"),
    ("prekrasny/nadherny", "wunderbar"),
    ("spat", "zuruck"),
    ("prazdniny", "die Ferien")
]

def quiz():
    score = 0
    total = len(sentences)
    random.shuffle(sentences)

    for word, translation in sentences:
        user_input = input(f"What is the translation of '{word}'? (Press 'q' to quit): ").strip()
        clear_terminal()
        if user_input.lower() == translation.lower():
            print("***************************************************")
            print(f"True. '{translation}' is correct.")
            score += 1
        else:
            print("***************************************************")
            print(f"False. The correct translation is '{translation}'.")

        if user_input.lower() == 'q':
            break

    print(f"You got {score} out of {total} correct.")


while True:
    print("Menu:")
    print("1. Start Quiz")
    print("2. Quit")

    choice = input("Enter your choice (1/2): ").strip()
    clear_terminal()
    if choice == '1':
        quiz()
    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

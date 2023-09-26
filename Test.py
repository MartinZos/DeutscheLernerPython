import random
import tkinter as tk
from tkinter import font as tkfont

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
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("German Vocabulary Quiz")
        self.root.geometry("600x400")  # Increase the window size

        self.score = 0
        self.current_question_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16, "bold"))  # Make text bold and bigger
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 14))  # Make text bigger
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        self.root.bind("<Right>", lambda event: self.next_question())  # Bind right arrow key to "Next Question"

        self.check_button = tk.Button(root, text="Check", command=self.check_answer, font=("Arial", 12))
        self.check_button.pack(pady=5)

        self.next_question_button = tk.Button(root, text="Next Question", command=self.next_question, font=("Arial", 12))
        self.next_question_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
        self.quit_button.pack(pady=20)

        # Create buttons for special characters
        special_chars = "ÄÖÜẞäöüß"
        special_char_frame = tk.Frame(root)
        special_char_frame.pack()

        for char in special_chars:
            char_button = tk.Button(special_char_frame, text=char, command=lambda c=char: self.insert_special_char(c),
                                    font=("Arial", 14), width=3, height=1, padx=5, pady=5)
            char_button.pack(side=tk.LEFT)

        self.update_question()

    def update_question(self):
        if self.current_question_index < len(sentences):
            self.question_label.config(text=f"What is the translation of '{sentences[self.current_question_index][0]}'?")
            self.answer_entry.delete(0, tk.END)
            self.question_label.config(fg="black")  # Reset text color
        else:
            self.question_label.config(text=f"You got {self.score} out of {len(sentences)} correct.")
            self.answer_entry.config(state=tk.DISABLED)
            self.check_button.config(state=tk.DISABLED)
            self.next_question_button.config(state=tk.DISABLED)
            self.quit_button.config(state=tk.DISABLED)

    def check_answer(self):
        user_input = self.answer_entry.get().strip()
        correct_answer = sentences[self.current_question_index][1].lower()

        if user_input.lower() == correct_answer:
            self.question_label.config(text=f"Correct. '{correct_answer}' is correct.", fg="green")
            self.score += 1
        else:
            self.question_label.config(text=f"Incorrect. The correct translation is '{correct_answer}'.", fg="red")

    def next_question(self):
        self.current_question_index += 1
        self.update_question()

    def insert_special_char(self, char):
        current_text = self.answer_entry.get()
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.insert(0, current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

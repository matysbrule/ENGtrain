import tkinter as tk
import random


# Fonction pour lire les mots depuis un fichier texte
def read_words_from_file(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            en, fr = line.strip().split(',')
            words.append({"en": en.strip(), "fr": fr.strip()})
    return words


class TranslationApp:
    def __init__(self, root, words):
        self.root = root
        self.root.title("Apprendre l'anglais")
        self.root.configure(bg='black')

        self.words = words
        self.score = 0

        self.word_label = tk.Label(root, text="", font=("Helvetica", 24), bg="black", fg="white")
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 18))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Vérifier", command=self.check_translation, font=("Helvetica", 18))
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="black", fg="white")
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Helvetica", 18), bg="black", fg="white")
        self.score_label.pack(pady=10)

        self.next_word()

    def next_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word['en'])
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

    def check_translation(self):
        user_translation = self.entry.get().strip().lower()
        correct_translation = self.current_word['fr']
        if user_translation == correct_translation:
            self.result_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"Incorrect! La bonne réponse est '{correct_translation}'", fg="red")
        self.score_label.config(text=f"Score: {self.score}")
        self.root.after(2000, self.next_word)


if __name__ == "__main__":
    words = read_words_from_file('words.txt')
    root = tk.Tk()
    app = TranslationApp(root, words)
    root.mainloop()

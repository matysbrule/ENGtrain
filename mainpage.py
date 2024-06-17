import tkinter as tk
import random

def read_words_from_file(filename):
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if ',' in line and line.strip():  # Vérifier que la ligne contient une virgule et n'est pas vide
                parts = line.strip().split(',')
                if len(parts) == 2:
                    en, fr = parts
                    words.append({"en": en.strip(), "fr": fr.strip()})
                else:
                    print(f"Ligne ignorée (mauvais format) : {line.strip()}")
            else:
                print(f"Ligne ignorée (pas de virgule ou vide) : {line.strip()}")
    return words


class TranslationApp:
    def __init__(self, root, words):
        self.root = root
        self.root.title("classic learning words")
        self.root.configure(bg='black')

        # Définir la taille de la fenêtre (largeur x hauteur)
        self.root.geometry("800x600")

        self.words = words
        self.score = 0
        self.current_word = None

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
        self.check_button.config(state=tk.NORMAL)  # Réactiver le bouton

    def check_translation(self):
        user_translation = self.entry.get().strip().lower()
        correct_translation = self.current_word['fr']
        if user_translation == correct_translation:
            self.result_label.config(text="Bien joué!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"La réponse c'était : '{correct_translation}' gros nullos", fg="red")
        self.score_label.config(text=f"Score: {self.score}")
        self.check_button.config(state=tk.DISABLED)  # Désactiver le bouton après un clic
        self.root.after(2000, self.next_word)


if __name__ == "__main__":
    words = read_words_from_file('words.txt')
    root = tk.Tk()
    app = TranslationApp(root, words)
    root.mainloop()

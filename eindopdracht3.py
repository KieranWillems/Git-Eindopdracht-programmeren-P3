galg = '''
import tkinter as tk
from tkinter import messagebox
import random

class Galgje:
    def __init__(self, woordenlijst):
        self.woorden = woordenlijst
        self.woord = random.choice(self.woorden)
        self.geraden_letters = []
        self.fouten = 0

    def controleer_gewonnen(self):
        for letter in self.woord:
            if letter not in self.geraden_letters:
                return False
        return True

    def handel_fout_af(self):
        self.fouten += 1
        if self.fouten == 6:
            messagebox.showinfo("Galgje", f"Helaas, je hebt verloren. Het woord was: {self.woord}")
            self.raam.quit()
        else:
            self.lbl_fouten.config(text=f"Fouten: {self.fouten}")

    def raad_letter(self):
        letter = self.entry_letter.get().lower()
        self.entry_letter.delete(0, tk.END)
        if not letter.isalpha() or len(letter) > 1:
            messagebox.showerror("Fout", "Voer een enkele letter in.")
            return
        if letter in self.geraden_letters:
            messagebox.showinfo("Galgje", f"De letter '{letter}' is al geraden.")
            return
        self.geraden_letters.append(letter)
        if letter not in self.woord:
            self.handel_fout_af()
        else:
            self.lbl_woord.config(text=self.get_woord_met_gaten())
            if self.controleer_gewonnen():
                messagebox.showinfo("Galgje", f"Gefeliciteerd, je hebt gewonnen! Het woord was: {self.woord}")
                self.raam.quit()

    def get_woord_met_gaten(self):
        woord_met_gaten = ""
        for letter in self.woord:
            if letter in self.geraden_letters:
                woord_met_gaten += letter + " "
            else:
                woord_met_gaten += "_ "
        return woord_met_gaten.strip()

    def start(self):
        self.raam = tk.Tk()
        self.raam.title("Galgje")

        self.lbl_woord = tk.Label(self.raam, text=self.get_woord_met_gaten(), font=("Helvetica", 20))
        self.lbl_woord.pack(pady=10)

        self.entry_letter = tk.Entry(self.raam, font=("Helvetica", 16), justify="center")
        self.entry_letter.pack(pady=10)

        self.btn_raden = tk.Button(self.raam, text="Raad letter", font=("Helvetica", 16), command=self.raad_letter)
        self.btn_raden.pack()

        self.lbl_fouten = tk.Label(self.raam, text=f"Fouten: {self.fouten}", font=("Helvetica", 16))
        self.lbl_fouten.pack(pady=10)

        self.raam.mainloop()

woordenlijst = ["hond", "kat", "olifant", "leeuw", "tijger", "giraffe", "aap", "neushoorn", "nijlpaard", "luipaard"]
galgje = Galgje(woordenlijst)
galgje.start()

'''

exec (galg)
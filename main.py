import random
import tkinter as tk

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Raad het Getal Spel")
        
        self.number = random.randint(1, 100)
        self.tries_left = 3
        
        self.label = tk.Label(self.master, text="Raad een getal tussen 1 en 100:")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.button = tk.Button(self.master, text="Raad!", command=self.check_guess)
        self.button.pack()
        
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()
        
        self.tries_label = tk.Label(self.master, text=f"Je hebt {self.tries_left} poging(en) over.")
        self.tries_label.pack()
        
    def check_guess(self):
        guess = int(self.entry.get())
        self.tries_left -= 1
        
        if guess == self.number:
            self.result_label.config(text="Je hebt het juiste getal geraden!")
            self.button.config(state="disabled")
            self.entry.config(state="disabled")
            return
        
        if self.tries_left == 0:
            self.result_label.config(text=f"Helaas, je hebt geen pogingen meer. Het getal was {self.number}.")
            self.button.config(state="disabled")
            self.entry.config(state="disabled")
            return
        
        if guess < self.number:
            self.result_label.config(text="Het getal is hoger!")
        else:
            self.result_label.config(text="Het getal is lager!")
        
        self.tries_label.config(text=f"Je hebt {self.tries_left} poging(en) over.")
        self.entry.delete(0, tk.END)
        
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
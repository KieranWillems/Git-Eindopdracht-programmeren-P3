import tkinter as tk
import random

dobbellijst = ["1", "2", "3", "4", "5", "6"]

window = tk.Tk()
window.title("DobbelGame")

frame = tk.Frame(master=window, borderwidth = 3)

frame.grid(row=0, column = 1)
vraag = tk.Label(
    master=frame,
    height = 7,
    width = 50,
    text="Als u wilt dobbelen, drukt u op de knop 'Dobbelen' ",
    bg="orange",
    font=("Arial", 30)
)
vraag.pack(fill=tk.BOTH, expand=True)

frame.grid(row=0, column = 2)
antwoord = tk.Label(
    master=frame,
    height = 7,
    width = 50,
    text="Hier komt het gerolde getal!",
    bg="blue",
    font=("Arial", 30)
)
antwoord.pack(fill=tk.BOTH, expand=True)

frame.grid(row=3, column=2)
Dobbelen = tk.Button(
    master=frame,
    width=20,
    height=5,
    text="Dobbelen"
)
Dobbelen.pack()

frame.grid(row=4, column=2)
clear = tk.Button(
    master=frame,
    width=20,
    height=5,
    text="Clear"
)
clear.pack()





def dobbel(event):
    rol = random.choice(dobbellijst)
    antwoord["text"] = "Het gerolde getal is " + rol + "."
    
def Clear(event):
    antwoord["text"] = ""
    

Dobbelen.bind("<Button-1>", dobbel)
clear.bind("<Button-1>", Clear)
window.mainloop()
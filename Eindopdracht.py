import tkinter as tk
import random

#Lijst voor de getallen van de dobbelsteen
dobbellijst = ["1", "2", "3", "4", "5", "6"]
#window maken
window = tk.Tk()
window.title("DobbelGame")  #-> De titel van de window



vraag = tk.Label( #-> Stukje tekst ter info voor de gebruiker
    height = 7,
    width = 50,
    text="Als u wilt dobbelen, drukt u op de knop 'Dobbelen' ",
    background="orange",
    foreground = "black",
    font=("Arial", 30)
)
vraag.pack(fill=tk.BOTH, expand=True) #-> zorgt ervoor dat de kleuren mee "rekken" als je de game grote maakt.
   
antwoord = tk.Label( #-<> Indicatie van waar de gerolde getallen komen
    height = 7,
    width = 50,
    text="Hier komt het gerolde getal!",
    bg="blue",
    font=("Arial", 30)
)
antwoord.pack(fill=tk.BOTH, expand=True) #-> zorgt ervoor dat de kleuren mee "rekken" als je de game grote maakt.

Dobbelen = tk.Button( #-> Knop om te dobbelen
    width=20,
    height=5,
    text="Dobbelen"
)
Dobbelen.pack()

clear = tk.Button( #-> Knop om te clearen.
    width=20,
    height=5,
    text="Clear"
)
clear.pack()

def dobbel(event): #-> deze functie zorgt ervoor dat er een random getal uit de list "dobbellijst" gekozen wordt en wordt laten zien
    rol = random.choice(dobbellijst)
    antwoord["text"] = "Het gerolde getal is " + rol + "."
    
def Clear(event):
    antwoord["text"] = ""
    

Dobbelen.bind("<Button-1>", dobbel) #-> De knop binden aan de functie "dobbel"
clear.bind("<Button-1>", Clear) #-> De knop binden aan de functie "Clear"
window.mainloop() #-> zorgt dat de Tkinter werkt
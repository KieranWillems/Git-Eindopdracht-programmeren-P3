import tkinter as tk #-> Tkinter importeren
import random #-> Random importeren voor later in de code




class Dobbelen: #-> Class aanmaken voor het menu
    def __init__(self, master): #-> master maken
        self.master = master
        master.title("DobbelGame")  #-> De titel van de window



        self.vraag = tk.Label( #-> Stukje tekst ter info voor de gebruiker
            height = 7,
            width = 50,
            text="Als u wilt dobbelen, drukt u op de knop 'Dobbelen' ",
            background="orange",
            foreground = "black",
            font=("Arial", 30)
        )
        self.vraag.pack(fill=tk.BOTH, expand=True) #-> zorgt ervoor dat de kleuren mee "rekken" als je de game grote maakt.
        
        self.antwoord = tk.Label( #-> Indicatie van waar de gerolde getallen komen
            height = 7,
            width = 50,
            text="Hier komt het gerolde getal!",
            bg="blue",
            font=("Arial", 30)
        )
        self.antwoord.pack(fill=tk.BOTH, expand=True) #-> zorgt ervoor dat de kleuren mee "rekken" als je de game grote maakt.

        self.Dobbelen = tk.Button( #-> Knop om te dobbelen
            width=20,
            height=5,
            text="Dobbelen"
        )
        self.Dobbelen.pack()

        self.clear = tk.Button( #-> Knop om te clearen.
            width=20,
            height=5,
            text="Clear"
        )
        self.clear.pack()

        self.dobbellijst = list(("1", "2", "3", "4", "5", "6")) #-> list aanmaken van de dobbelsteen
        def dobbel(event): #-> deze functie zorgt ervoor dat er een random getal uit de list "dobbellijst" gekozen wordt en wordt laten zien
            rol = random.choice(self.dobbellijst)
            self.antwoord["text"] = "Het gerolde getal is " + rol + "."
            
        def Clear(event): #-> De tekst waar het gerolde getal staat wordt gecleared en het er staat een lege tekst
            self.antwoord["text"] = ""
            

        self.Dobbelen.bind("<Button-1>", dobbel) #-> De knop binden aan de functie "dobbel"
        self.clear.bind("<Button-1>", Clear) #-> De knop binden aan de functie "Clear"
        


if __name__ == '__main__': #-> code laten werken.
    root = tk.Tk()
    app = Dobbelen(root)
    root.mainloop()
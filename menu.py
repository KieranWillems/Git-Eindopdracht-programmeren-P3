from tkinter import *
from Dobbelen import *
from main import *
from eindopdracht3 import *

# Maak een nieuw window met een titel
window = Tk()
window.title("Menu")

# Functies voor het menu
def dobbelen():
    frame_thing_2.pack_forget()
    frame_Galgje.pack_forget()
    exec(dobbel)


def guessinggame():
    frame_Galgje.pack_forget()
    frame_Dobbelen.pack_forget()
    exec(getalraad)

def Galg():
    frame_thing_2.pack_forget()
    frame_Dobbelen.pack_forget()
    exec(galg)
    

# Menu maken
menubar = Menu(window)
window.config(menu=menubar)


# Menu items maken
mainmenu = Menu(menubar)
mainmenu.add_command(label="Dobbelspel", command=dobbelen)
mainmenu.add_command(label="Getallen raden", command=guessinggame)        
mainmenu.add_command(label="Galgje", command=Galg)    
mainmenu.add_separator()
mainmenu.add_command(label="Exit", command=window.quit)
# Menu toevoegen aan menubar
menubar.add_cascade(label="Tool", menu=mainmenu)

# FRAME VOOR THING 1 --------------------------------
frame_Dobbelen = Frame(borderwidth=10)
label_1 = Label(frame_Dobbelen, text="DobbelGame", bg="red", fg="yellow", width=20, height=8)
label_1.pack()

# FRAME VOOR THING 2 --------------------------------
frame_thing_2 = Frame(borderwidth=10)
label_2 = Label(frame_thing_2, text="GuessingGame", bg="red", fg="yellow", width=20, height=8)
label_2.pack()

frame_Galgje = Frame(borderwidth=10)
label_3 = Label(frame_Galgje, text="Galgje", bg="red", fg="yellow", width=20, height=8)
label_3.pack()

# MAIN --------------------------------
# Begin met frame 1
Galg()
# Start the application
window.mainloop()
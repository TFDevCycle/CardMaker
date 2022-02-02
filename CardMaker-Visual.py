from tkinter import *
from tkinter.ttk import Combobox

app = Tk()
app.geometry("300x300")

Select_CardType = Combobox(app, values=['Monster', 'Spell', 'Trap']).pack()
app.mainloop()
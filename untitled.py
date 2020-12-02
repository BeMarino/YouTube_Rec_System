import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('300x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

fontExample = ("Courier", 16, "bold")
comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"],
                            font = fontExample)

app.option_add('*TCombobox*Listbox.font', fontExample)

comboExample.grid(column=0, row=1)

app.mainloop()
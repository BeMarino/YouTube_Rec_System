import tkinter as tk
from tkinter import ttk

def callback(input): 
      
    if input.isdigit(): 
        print(input) 
        return True
                          
    elif input == "": 
        print(input) 
        return True
  
    else: 
        print(input) 
        return False

def save(accountCombo,methodCombo,stepsEntry,timeEntry,queryEntry):
    print("jhdbjk")



accountList=["account iscritto ad alcuni canali ","account pulito"]

methodList=["Per successivo","Tutti i correlati"]

window = tk.Tk() 

window.title("New session setup")
window.geometry("450x230")


fontExample = ("Courier", 16, "bold")

#----creazione Combobox per la selezione dell'account con cui effettuare la sessione----------
accountLabel = tk.Label(window,text = "Seleziona tipologia account")
accountLabel.place(x=20,y=10,width=150)
accountCombo = ttk.Combobox(window,values=accountList)
accountCombo.place(x=20,y=30,width=200)
#----/creazione Combobox per la selezione dell'account con cui effettuare la sessione----------

#----creazione Combobox per la selezione del metodo con cui effettuare la sessione----------
methodLabel = tk.Label(window,text = "Seleziona metodo esplorazione")
methodLabel.place(x=245,y=10,width=180)
methodCombo = ttk.Combobox(window,values=methodList)
methodCombo.place(x=250,y=30,width=180)
#----/creazione Combobox per la selezione del metodo con cui effettuare la sessione----------

#----creazione casella di testo per inserimento del numero di passi da effettuare durante la sessione----------
stepsLabel = tk.Label(window,text = "Inserisci il numero di passi")
stepsLabel.place(x=230,y=60,width=180)
stepsEntry = ttk.Entry(window) 
stepsEntry.place(x = 250, y = 80) 
reg = window.register(callback) 
stepsEntry.config(validate ="key",  validatecommand =(reg, '%P')) 
#----/creazione casella di testo per inserimento del numero di passi da effettuare durante la sessione----------
  
#----creazione casella di testo per inserimento del tempo di visualizzazione dei video----------
timeLabel = tk.Label(window,text = "Inserisci tempo visualizzazione in secondi")
timeLabel.place(x=15,y=60,width=230)
timeEntry = ttk.Entry(window) 
timeEntry.place(x = 20, y = 80) 
reg = window.register(callback) 
timeEntry.config(validate ="key",  validatecommand =(reg, '%P')) 
#----/creazione casella di testo per inserimento del tempo di visualizzazione dei video----------
  
#----creazione casella di testo per inserimento della query di ricerca----------
queryLabel = tk.Label(window,text = "Inserisci query di ricerca")
queryLabel.place(x=-8,y=110,width=180)
queryEntry = ttk.Entry(window) 
queryEntry.place(x =20 , y = 130,width=300) 
#----/creazione casella di testo per inserimento della query di ricerca----------


saveButton=ttk.Button(window,text="Save setup",command=lambda:save(accountCombo,methodCombo,stepsEntry,timeEntry,queryEntry))
saveButton.place(x=180, y=180)
window.mainloop()

'''print('Seleziona l\'account da utilizzare, inserisci:\n 1. per l\'account iscritto a canali "controversi"\n 2. per l\'account "pulito"  ')
account=int(input())
metodo=input('Seleziona il metodo di esplorazione, inserisci:\n 1. per seguire i video successivi\n 2. per guardare i correlati  ')
tempo_osservazione=int(input('Inserisci il tempo di osservazione desiderato (in secondi):'))
query=input('Inserisci la parola o frase che vuoi cercare su youtube:')
steps=int(input('Inserisci il numero di steps da eseguire:'))

if(metodo=="1"):
    exec(open("exploreByNext.py").read(),{'account':accountList[account-1],'tempo_osservazione':tempo_osservazione,'steps':steps})
else:
    exec(open("exploreByRelated.py").read(),{'account':accountList[account-1],'tempo_osservazione':tempo_osservazione,'steps':steps})'''
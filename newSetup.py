import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from lib import create_connection
from config import account_list

def callback(input): 
      
    if input.isdigit(): 
        
        return True
                          
    elif input == "": 
       
        return True
  
    else: 
        
        return False



def save(account,method,steps,time,query,iterations,frequency,gradeFrequency):

    if None not in [account,method,steps,time,query,frequency,gradeFrequency]:
        forConversion={"Minutes":60,"Hours":3600,"Days":3600*24}
        DBquery="insert into setupsessione(account,tipo,query,steps,viewTime,status,frequency,iterations) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        connection= create_connection("localhost","root","","tesi")
        cursor=connection.cursor()
        
        cursor.execute(DBquery,[account,method,query,steps,time,"ready",int(frequency)*int(forConversion[gradeFrequency]),iterations])
        connection.commit()

        messagebox.showinfo("Info","Your setup has been correctly saved")
    else:
        messagebox.showerror("Error", "Error, please check your data and repeat.")

    


methodList={" By next one":1," Every related video":2}



window = tk.Tk() 

window.title("New session setup")
window.geometry("450x320")


fontExample = ("Courier", 16, "bold")

#----creazione Combobox per la selezione dell'account con cui effettuare la sessione----------
accountLabel = tk.Label(window,text = "Select account")
accountLabel.place(x=20,y=10,width=150)
accountCombo = ttk.Combobox(window,values=list(account_list.keys()))
accountCombo.place(x=20,y=30,width=200)

#----/creazione Combobox per la selezione dell'account con cui effettuare la sessione----------

#----creazione Combobox per la selezione del metodo con cui effettuare la sessione----------
methodLabel = tk.Label(window,text = "Select exploration method")
methodLabel.place(x=245,y=10,width=180)
methodCombo = ttk.Combobox(window,values=list(methodList.keys()))
methodCombo.place(x=250,y=30,width=180)
#----/creazione Combobox per la selezione del metodo con cui effettuare la sessione----------

#----creazione casella di testo per inserimento del numero di passi da effettuare durante la sessione----------
stepsLabel = tk.Label(window,text = "Insert number of steps")
stepsLabel.place(x=220,y=60,width=180)
stepsEntry = ttk.Entry(window) 
stepsEntry.place(x = 250, y = 80) 
reg = window.register(callback) 
stepsEntry.config(validate ="key",  validatecommand =(reg, '%P')) 
#----/creazione casella di testo per inserimento del numero di passi da effettuare durante la sessione----------
  
#----creazione casella di testo per inserimento del tempo di visualizzazione dei video----------
timeLabel = tk.Label(window,text = "Insert viewTime (seconds)")
timeLabel.place(x=-5,y=60,width=230)
timeEntry = ttk.Entry(window) 
timeEntry.place(x = 20, y = 80) 
reg = window.register(callback) 
timeEntry.config(validate ="key",  validatecommand =(reg, '%P')) 
#----/creazione casella di testo per inserimento del tempo di visualizzazione dei video----------
  
#----creazione casella di testo per inserimento della query di ricerca----------
queryLabel = tk.Label(window,text = "Insert session query ")
queryLabel.place(x=-8,y=110,width=180)
queryEntry = ttk.Entry(window) 
queryEntry.place(x =20 , y = 130,width=300) 
#----/creazione casella di testo per inserimento della query di ricerca----------

#----creazione casella di testo per inserimento del numero di iterazioni----------
iterationsLabel = tk.Label(window,text = "Number of repetitions")
iterationsLabel.place(x=0,y=160,width=200)
iterationsEntry = ttk.Entry(window) 
iterationsEntry.place(x =20 , y = 180,width=50) 
reg = window.register(callback) 
iterationsEntry.config(validate ="key",  validatecommand =(reg, '%P')) 
#----/creazione casella di testo per inserimento del numero di iterazioni----------

#----creazione casella di testo per inserimento della frequenza----------
frequencyLabel = tk.Label(window,text = "Choose interval between repetitions?")
frequencyLabel.place(x=2,y=210,width=230)
frequencyEntry = ttk.Entry(window) 
frequencyEntry.place(x =20 , y = 230,width=80) 
reg = window.register(callback) 
frequencyEntry.config(validate ="key",  validatecommand =(reg, '%P')) 

frequencyCombo = ttk.Combobox(window,values=["Minutes","Hours","Days"])
frequencyCombo.place(x=105,y=230,width=180)
#----/creazione casella di testo per inserimento della frequenza----------

saveButton=ttk.Button(window,text="Save setup",command= lambda:save(accountCombo.get(),methodList.get(methodCombo.get()),stepsEntry.get(),timeEntry.get(),queryEntry.get(),iterationsEntry.get(),frequencyEntry.get(),frequencyCombo.get()))
saveButton.place(x=180, y=270)

window.mainloop()

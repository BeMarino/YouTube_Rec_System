import mysql.connector
from mysql.connector import Error
from lib import create_connection,checkForOngoing,checkForReady,aggiorna_setupsessione
import subprocess
import time
import json
import sys
from datetime import datetime

# sys.stdout=open("logFile/main.txt","a+")
# sys.stderr=open("errorLogFile/main.txt","a+")

print("Ora esecuzione: "+str(datetime.now())+"\n")

#-------connessione al database------------
connection= create_connection("localhost","root","","tesi")
cursor=connection.cursor()

method={1:"exploreByNext.py",2:"exploreByRelated.py"}#dizionario utilizzato per selezionare il tipo di esplorazione in base al dato presente nel db

#-------Estrazione configurazione dal DB e avvio procedura-----------
#----Query utilizzata per estrarre una configurazione pronta per essere eseguita-----
while 1:
    connection= create_connection("localhost","root","","tesi")
    cursor=connection.cursor()

    setup_list=checkForOngoing(connection,cursor)
    i=0
    print("Sessioni ongoing da eseguire: "+str(len(setup_list))+"\n")
    for setup in setup_list:
    
        print(setup['account'])
    
        startedAtTime=aggiorna_setupsessione(setup,connection,cursor)
        setup["startedAtTime"]=startedAtTime
        p=subprocess.Popen(['python', method[setup['tipo']]]+[json.dumps(setup)],stdout=open("logFile/log"+str(i)+".txt","w"),stderr=open("errorLogFile/err_log"+str(i)+".txt","w"))
        i+=1

    setup_list=checkForReady(connection,cursor)
    i=0
    print("Sessioni ready da eseguire: "+str(len(setup_list))+"\n\n\n***********************************\n\n\n")
    for setup in setup_list:
      
        
        startedAtTime=aggiorna_setupsessione(setup,connection,cursor)
        setup["startedAtTime"]=startedAtTime
        p=subprocess.Popen(['python', method[setup['tipo']]]+[json.dumps(setup)],stdout=open("logFile/log"+str(i)+".txt","w"),stderr=open("errorLogFile/err_log"+str(i)+".txt","w"))
        i+=1
        
    time.sleep(60)
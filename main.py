import mysql.connector
from mysql.connector import Error
from lib import create_connection,checkForOngoing,checkForReady,aggiorna_setupsessione
from multiprocessing import Process
import subprocess
import time
import json


#-------connessione al database------------
connection= create_connection("localhost","root","","tesi")
cursor=connection.cursor()

method={1:"exploreByNext.py",2:"exploreByRelated.py"}#dizionario utilizzato per selezionare il tipo di esplorazione in base al dato presente nel db

#-------Estrazione configurazione dal DB e avvio procedura-----------
#----Query utilizzata per estrarre una configurazione pronta per essere eseguita-----
setup_list=checkForOngoing(connection,cursor)
i=0
for setup in setup_list:
   
    print(setup['account'])
    
    #Process(target=exec(opern))
    aggiorna_setupsessione(setup,connection,cursor)
    p=subprocess.Popen(['python', method[setup['tipo']]]+[json.dumps(setup)],stdout=open("log"+str(i)+".txt","w"),stderr=open("err_log"+str(i)+".txt","w"))
    i+=1
    #exec(open(method[setup['tipo']]).read(),{'account':setup['account'],'query':setup['query'],'tempo_osservazione':setup['viewTime'],'steps':setup['steps'],'idSetup':setup['id']})
    #---------/Estrazione configurazione dal DB e avvio procedura-----------
#for setup in setup_list:   
    #setup_list=checkForReady(connection,cursor)
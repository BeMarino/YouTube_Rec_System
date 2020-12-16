import mysql.connector
from mysql.connector import Error
import lib
import time

#-------connessione al database------------
connection= lib.create_connection("localhost","root","","tesi")
cursor=connection.cursor()

method={1:"exploreByNext.py",2:"exploreByRelated.py"}#dizionario utilizzato per selezionare il tipo di esplorazione in base al dato presente nel db

#-------Estrazione configurazione dal DB e avvio procedura-----------
#----Query utilizzata per estrarre una configurazione pronta per essere eseguita-----
query="select id,account,tipo,query,steps,viewTime,iterations,executedTimes from setupsessione where status='ready' limit 1 "
cursor.execute(query)

#---Creo un dizionario che ha come chiavi i nomi delle colonne del db e come valori i dati presenti all'interno della tabella----
desc = cursor.description
column_names = [col[0] for col in desc]
setup = [dict(zip(column_names, row))  
        for row in cursor.fetchall()][0]

query_setup="update setupsessione set executedTimes=%s, status=%s where id=%s"

if(setup['iterations']-setup['executedTimes']==1):  
    
    cursor.execute(query_setup,[setup['executedTimes']+1,"completed",setup['id']])
else:
    cursor.execute(query_setup,[setup['executedTimes']+1,"ongoing",setup['id']])
print(time.time())
cursor.execute("INSERT INTO sessione(setupId,startedAt) VALUES(%s,%s)",[setup['id'],time.time()])
connection.commit()


exec(open(method[setup['tipo']]).read(),{'account':setup['account'],'query':setup['query'],'tempo_osservazione':setup['viewTime'],'steps':setup['steps'],'idSetup':setup['id']})
#---------/Estrazione configurazione dal DB e avvio procedura-----------
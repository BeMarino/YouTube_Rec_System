
import mysql.connector
from mysql.connector import Error
import lib
connection= lib.create_connection("localhost","root","","tesi")
cursor=connection.cursor()
query_setup="update setupsessione set executedTimes=%s, status=%s where id=%s"
cursor.execute(query_setup,[1,"completed",8])
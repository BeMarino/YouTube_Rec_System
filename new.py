
import mysql.connector
from mysql.connector import Error
import lib
connection= lib.create_connection("localhost","root","","tesi")
cursor=connection.cursor()
last_session_query="select max(id) from sessione"
cursor.execute(last_session_query)
result=cursor.fetchone()[0]
print(result)
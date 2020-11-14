import json
import googleapiclient.discovery
import csv
import mysql.connector
from mysql.connector import Error
import lib

api_key="AIzaSyCWH5-fbx-6X4GHB3fc291PdVOBCyYOQGQ"

connection= lib.create_connection("localhost","root","","Tesi Benny")
with open("results/account1/next_exploration.csv","r") as risultati:
    reader=csv.reader(risultati)
    for row in reader:
        print(row)

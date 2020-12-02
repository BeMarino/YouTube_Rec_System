import json
import googleapiclient.discovery
import csv
import mysql.connector
from mysql.connector import Error
import lib
import time
import datetime
accountList=["emailperlatesi@gmail.com","emailperlatesi2@gmail.com"]
files=["next_exploration.csv","by_related_exploration.csv"]
api_key="AIzaSyCWH5-fbx-6X4GHB3fc291PdVOBCyYOQGQ"
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

connection= lib.create_connection("localhost","root","","tesi")
cursor=connection.cursor()


session_query="insert into sessione(account,tipo,query,elapsed_time) values(%s,%s,%s,%s)"
cursor.execute(session_query,[account,tipo,query,tempo])
connection.commit()


last_session_query="select max(id) from sessione"
cursor.execute(last_session_query)
sessione=cursor.fetchone()[0]
query="Insert into video(id,title,description,publisher_id,publisher,watched_id,suggested_times,categoryId,categoryTitle,session) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for account in accountList:
    for f in files:
        with open("results/"+account+"/"+f,"r") as risultati:
            reader=csv.reader(risultati)
            i=0
            for row in reader:
                if("&" in row[1]):
                    row[1]=row[1][0:row[1].index("&")]
                print(row[1])
                if(i!=0):
                    if(not lib.isInDb(row[1],cursor)):
                        
                        video_request=youtube.videos().list(
                            part="snippet",
                            id=row[1]
                        )

                        video_response = video_request.execute()
                        if(video_response["pageInfo"]["totalResults"]>0):
                            category=video_response["items"][0]["snippet"]["categoryId"]
                            print(video_response)               
                            category_request = youtube.videoCategories().list(
                                    part="snippet",
                                    id=category
                            )
                            category_response = category_request.execute()
                            print(category_response)
                            
                            values=[
                                row[1],
                                video_response["items"][0]["snippet"]['title'],
                                video_response["items"][0]["snippet"]['description'],
                                video_response["items"][0]["snippet"]['channelId'],
                                video_response["items"][0]["snippet"]['channelTitle'],
                                row[0],
                                1,
                                category,
                                category_response["items"][0]["snippet"]["title"],
                                sessione
                            ]
                            
                            cursor.execute(query,values)
                            connection.commit()
                    else:
                        cursor.execute("update video set suggested_times=%s where id =%s",[lib.getSuggestedTimes(row[1],cursor)+1,row[1]])
                i+=1
                print(i)

        

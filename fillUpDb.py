import googleapiclient.discovery
import csv
import lib
import time
import re
from config import yt_api_key



def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


files=["next_exploration.csv","by_related_exploration.csv"]

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=yt_api_key)

connection= lib.create_connection("localhost","root","","tesi")
cursor=connection.cursor()

query="Insert into video(id,title,description,publisher_id,publisher,watched_id,suggested_times,categoryId,categoryTitle,idSetup) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

with open("results/"+account+"/"+files[tipo-1],"r") as risultati:
    reader=csv.reader(risultati)
    i=0
    for row in reader:
        
        if("&" in row[1]):
            row[1]=row[1][0:row[1].index("&")]
       
        
        if(not lib.isInDb(row[1],cursor)):
            
            video_request=youtube.videos().list(
                part="snippet",
                id=row[1]
            )
            
            video_response = video_request.execute()
            
            
            if(video_response["pageInfo"]["totalResults"]>0):
                
                deEmojify(video_response["items"][0]["snippet"]['title']),
                deEmojify(video_response["items"][0]["snippet"]['description']),
                deEmojify(video_response["items"][0]["snippet"]['channelId']),
                deEmojify(video_response["items"][0]["snippet"]['channelTitle'])    
                category=video_response["items"][0]["snippet"]["categoryId"]
                            
                category_request = youtube.videoCategories().list(
                        part="snippet",
                        id=category
                )
                category_response = category_request.execute()
                
                
                values=[
                    row[1],
                    deEmojify(video_response["items"][0]["snippet"]['title']),
                    deEmojify(video_response["items"][0]["snippet"]['description']),
                    deEmojify(video_response["items"][0]["snippet"]['channelId']),
                    deEmojify(video_response["items"][0]["snippet"]['channelTitle']),
                    row[0],
                    1,
                    category,
                    category_response["items"][0]["snippet"]["title"],
                    row[6]
                ]
                
                cursor.execute(query,values)
                connection.commit()
        else:
            cursor.execute("update video set suggested_times=%s where id =%s",[lib.getSuggestedTimes(row[1],cursor)+1,row[1]])
    
    

        

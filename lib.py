import isodate
import json
import googleapiclient.discovery    
import csv
import time
import mysql.connector
from mysql.connector import Error
from selenium.common import exceptions


def create_connection(host_name, user_name, user_password,db):

    connection = None

    try:

        connection = mysql.connector.connect(

            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db,
            buffered=True

        )

        print("Connection to MySQL DB successful")

    except Error as e:

        print(f"The error '{e}' occurred")


    return connection

def isInDb(video_id,cursor):
    cursor.execute("select * from video where id = %s",[video_id])
    if(cursor.rowcount>0):
        return 1
    else:
        return 0


def getSuggestedTimes(video_id,cursor):
    cursor.execute("select suggested_times from video where id=%s",[video_id])
    return cursor.fetchone()[0]


def getDuration(id):
   
    api_key="AIzaSyCWH5-fbx-6X4GHB3fc291PdVOBCyYOQGQ"

    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)
    
    request = youtube.videos().list(
        part="contentDetails",
        id=id
    )
    response=request.execute()
    time.sleep(3)
    dur=isodate.parse_duration(response['items'][0]["contentDetails"]["duration"])
    return int(dur.total_seconds())
 
def login(driver,email,password):
    elem = driver.find_element_by_id("action-button")
    elem.find_element_by_class_name("yt-simple-endpoint").click()
    elem=driver.find_element_by_id("identifierId")
    elem.send_keys(email)
    driver.find_element_by_id("identifierNext").find_element_by_tag_name("button").click()
    time.sleep(2)
    driver.find_element_by_id("password").find_element_by_tag_name("input").send_keys(password)
    driver.find_element_by_id("passwordNext").find_element_by_tag_name("button").click()

#Recupera gli id dei video presenti nella lista a parametro, li stampa nel csv e ritorna il primo video suggerito
def getHomeVideosId(driver,file): 
    videos=driver.find_element_by_id("contents").find_elements_by_id("content")
    next_video=""
    writer=csv.writer(file)
    i=0
    for element in videos:
        try:    

            url=element.find_element_by_id("thumbnail").get_attribute("href") 
           
            if next_video=="":
                next_video=element
                writer.writerow(["",url[url.index("=")+1:],1,1,time.time() ])
            else:
                writer.writerow(["",url[url.index("=")+1:],0,1,time.time() ])
            i+=1
        except exceptions.NoSuchElementException:
            print("elemento non trovato")
        print(i)
    return next_video


#-----getNextVideo scrive sul csv la lista di tutti i video che vengono consigliati durante la visualizzazione di un video e 
#     restituisce l'id del video che verrà automaticamente riprodotto una volta finito il video che si sta visualizzando-----
def getNextVideo(driver,file,watched):
    
    next_=driver.find_element_by_id("related").find_element_by_id("items").find_element_by_id("contents")
    next_video=next_.find_element_by_id("thumbnail").get_attribute("href")
    related_videos=driver.find_element_by_id("related").find_element_by_id("items").find_elements_by_id("dismissable")
    print(next_video)

    writer=csv.writer(file)
    writer.writerow([watched,next_video[next_video.index("=")+1:],1,0,time.time() ])

    for v in related_videos[1:]:
        relatedVideoId=v.find_element_by_id("thumbnail").get_attribute("href")[v.find_element_by_id("thumbnail").get_attribute("href").index("=")+1:]
        if("&" in relatedVideoId):
            relatedVideoId=relatedVideoId[0:relatedVideoId.index("&")]
        writer.writerow([watched,relatedVideoId,0,0,time.time() ])
        
        print(relatedVideoId)
    
    return next_

#-----getNextVideo scrive sul csv la lista di tutti i video che vengono consigliati durante la visualizzazione di un video e 
#     restituisce l'intera lista dei video suggeriti-----
def getRelatedVideos(driver,file,watched):
    
    related_videos=driver.find_element_by_id("related").find_element_by_id("items")
    next_=related_videos.find_element_by_id("contents")
    next_video=next_.find_element_by_id("thumbnail").get_attribute("href")
    related_videos=driver.find_element_by_id("related").find_elements_by_id("items")
    writer=csv.writer(file)
    writer.writerow([watched,next_video[next_video.index("=")+1:],1,0,time.time() ])

    for v in related_videos.find_elements_by_id("dismissable"):
        id=v.find_element_by_id("thumbnail").get_attribute("href")[v.find_element_by_id("thumbnail").get_attribute("href").index("=")+1:]
        if("&" in id):
            id=id[0:id.index("&")]
        writer.writerow([watched,id,0,0,time.time()])
      
    
    return related_videos

#----la funzione config setta i parametri di esplorazione in base ad un file di configurazione fornito in input----
def config():
    config={}
    with open("config.txt","r") as f:
        for line in f.readlines():
            config[line[0:line.index(":")]]=line[line.index(":")+1:line.index(";")]
    return config
            

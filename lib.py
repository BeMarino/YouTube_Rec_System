
import isodate
import json
import googleapiclient.discovery    
from datetime import datetime
import csv
import time
from selenium.common import exceptions

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

def getHomeVideosId(videos, file): #Recupera gli id dei video presenti nella lista a parametro, li stampa nel csv e ritorna il primo video suggerito
    next_video=""
    writer=csv.writer(file)
    for element in videos:
        try:    

            url=element.find_element_by_id("thumbnail").get_attribute("href") 
           
            if next_video=="":
                next_video=element
                writer.writerow(["",url[url.index("=")+1:],1,1,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")])
            else:
                writer.writerow(["",url[url.index("=")+1:],0,1,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")])
        except exceptions.NoSuchElementException:
            print("elemento non trovato")
    
    return next_video

def getRelatedVideos(driver,file,watched):
    
    next_=driver.find_element_by_id("related").find_element_by_id("items").find_element_by_id("contents")
    next_video=next_.find_element_by_id("thumbnail").get_attribute("href")
    related_videos=driver.find_element_by_id("related").find_element_by_id("items").find_elements_by_id("dismissable")
    print(next_video)

    writer=csv.writer(file)
    writer.writerow([watched,next_video[next_video.index("=")+1:],1,0,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")])

    for v in related_videos[1:]:
        relatedVideoId=v.find_element_by_id("thumbnail").get_attribute("href")[v.find_element_by_id("thumbnail").get_attribute("href").index("=")+1:]
        writer.writerow([watched,relatedVideoId,0,0,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")])
        
        print(relatedVideoId)
    
    return next_

def config():
    config={}
    with open("config.txt","r") as f:
        for line in f.readlines():
            config[line[0:line.index(":")]]=line[line.index(":")+1:line.index(";")]
    return config
            

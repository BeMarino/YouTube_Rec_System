import googleapiclient.discovery   
import lib
from selenium import webdriver
from selenium.common import exceptions
import time
config=lib.config()

steps=int(config["steps"])
email=config["email"]
password=config["password"]
tempo_osservazione=int(config["tempo_osservazione"])
base_url="https://www.youtube.com/watch?v="
driver = webdriver.Firefox()
driver.get("http://www.youtube.com")
driver.implicitly_wait(5)



assert "YouTube" in driver.title

#-----Accesso account-------
lib.login(driver,email,password)
#-----/Accesso account------

next_video=""

i=0
videos=driver.find_element_by_id("contents").find_elements_by_id("content")
for element in videos:
    try:    

        url=element.find_element_by_id("thumbnail").get_attribute("href") 
        
        if next_video=="":
            next_video=element
            break
        i+=1
    except exceptions.NoSuchElementException:
        print("elemento non trovato")
element.click()

related_videos=driver.find_element_by_id("related").find_element_by_id("items")
next_=related_videos.find_element_by_id("contents")
next_video=next_.find_element_by_id("thumbnail").get_attribute("href")



next_=driver.find_element_by_id("related").find_element_by_id("items").find_element_by_id("contents")
next_video=next_.find_element_by_id("thumbnail").get_attribute("href")
related_videos=driver.find_element_by_id("related").find_element_by_id("items").find_elements_by_id("dismissable")


for v in related_videos[1:]:
    relatedVideoId=v.find_element_by_id("thumbnail").get_attribute("href")[v.find_element_by_id("thumbnail").get_attribute("href").index("=")+1:]
    if("&" in relatedVideoId):
        relatedVideoId=relatedVideoId[0:relatedVideoId.index("&")]
    print(relatedVideoId+"fff")
    
    
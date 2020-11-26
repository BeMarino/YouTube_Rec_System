from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import lib
import csv
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
#-----Ricerca dei video in home page e visualizzazione del primo consigliato-----



with open("results/account1/next_exploration.csv","a+",newline='') as session:
   
    watched=lib.getHomeVideosId(driver,session)
    watched.click()
        #-----/Ricerca dei video in home page e visualizzazione del primo consigliato-----
    while steps>0:
        
        currentVideoId=driver.current_url[driver.current_url.index("=")+1:]
        lenght=lib.getDuration(currentVideoId)
        time.sleep(3)
        next_video=lib.getNextVideo(driver,session,currentVideoId)
        

        if lenght>tempo_osservazione:
            time.sleep(tempo_osservazione)
        else:
            time.sleep(lenght-lenght/4)
        steps-=1
        next_video.click()

assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()



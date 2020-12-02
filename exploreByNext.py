from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import lib
import csv
import time




password="t3stings3lenium"

base_url="https://www.youtube.com/watch?v="
driver = webdriver.Firefox()
driver.get("http://www.youtube.com")
driver.implicitly_wait(5)


assert "YouTube" in driver.title

#-----Accesso account-------
lib.login(driver,account,password)
#-----/Accesso account------
#-----Ricerca dei video in home page e visualizzazione del primo consigliato-----



with open("results/"+account+"/next_exploration.csv","a+",newline='') as session:
   
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

#------Una volta terminati i passi avvio la procedura per inserire i dati relativi ai video nel database-------
exec(open("fillUpDb.py").read(),{"account":account,"tipo":"next","query":"","tempo":tempo_osservazione})



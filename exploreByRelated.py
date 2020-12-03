from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import lib
import csv
import time


password="t3stings3lenium"

base_url="https://www.youtube.com/watch?v="
driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
#driver.implicitly_wait(5)


assert "YouTube" in driver.title

#-----Accesso account-------
lib.login(driver,account,password)
#-----/Accesso account------



with open("results/account1/by_related_exploration.csv","a+",newline='') as session:
    #-----Ricerca dei video in home page e visualizzazione del primo consigliato-----
    toWatch=lib.getHomeVideosId(driver,session)
    toWatch.click()
    currentVideoId=driver.current_url[driver.current_url.index("=")+1:]
    time.sleep(5)
    related_videos=lib.getRelatedVideos(driver,session,currentVideoId)
    print(related_videos)
    i=0
    while steps>0:
        
        try: 
            time.sleep(8)  
            skipButton=driver.find_element_by_class_name("ytp-ad-skip-button ytp-button")
            skipButton.click()
            print("Pubblicita' skippata")
        except exceptions.NoSuchElementException:
            print("Il video non contiene pubblicita'")

        currentVideoId=driver.current_url[driver.current_url.index("=")+1:]
        lenght=lib.getDuration(currentVideoId)
        
        
        if lenght>tempo_osservazione:
            time.sleep(tempo_osservazione)
        else:
            time.sleep(lenght-lenght/4)
        steps-=1
        if i>=1:
            driver.back()
            time.sleep(5)
        related_videos[i].click()
        i+=1
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()

#------Una volta terminati i passi avvio la procedura per inserire i dati relativi ai video nel database------- 
#exec(open("fillUpDb.py").read(),{"account":account,"tipo":"related","query":"","tempo":tempo_osservazione})


from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import lib
import csv
import time




password="t3stings3lenium"

base_url="https://www.youtube.com/watch?v="
#options =Options()
#options.add_argument("--lang=it")
#driver = webdriver.Firefox(options=options)
profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'it-IT, it')
driver = webdriver.Firefox(firefox_profile=profile)

#------- carico estensione per bloccare le pubblicità-------#
driver.install_addon("C:\\Users\\Benny\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\vj6f2v1i.default-release-1605184895016\\extensions\\uBlock0@raymondhill.net.xpi", temporary=True)
driver.get("http://www.youtube.com")
driver.implicitly_wait(5)


assert "YouTube" in driver.title

#-----Accesso account-------
lib.login(driver,account,password)
#-----/Accesso account------
#-----Ricerca dei video in home page e visualizzazione del primo consigliato-----



with open("results/"+account+"/next_exploration.csv","a+",newline='') as session:
   
    watched=lib.getHomeVideosId(driver,session,idSetup)
    

    if(query):
        lib.search(driver,query,Keys.ENTER)
        lib.getQueryResult(driver,session,idSetup).click()
    else:
        watched.click()
    #-----/Ricerca dei video in home page e visualizzazione del primo consigliato-----
    while steps>0:
        
        currentVideoId=driver.current_url[driver.current_url.index("=")+1:]
        length=lib.getDuration(currentVideoId)
        time.sleep(3)
        next_video=lib.getNextVideo(driver,session,currentVideoId,tempo_osservazione,idSetup)
        
        if length>0:
            if length>tempo_osservazione:
                time.sleep(tempo_osservazione)
            else:
                time.sleep(length-length/4)
            steps-=1
            next_video.click()
        else:
            steps-=1
            next_video.click()

assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()
lib.setSessionEndTime(idSetup)
#------Una volta terminati i passi avvio la procedura per inserire i dati relativi ai video nel database-------
exec(open("fillUpDb.py").read(),{"account":account,"tipo":1,"query":query,"idSetup":idSetup})



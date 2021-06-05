from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.options import Options
import lib
import csv
import time
import sys
import json
from config import account_list
import os


base_url="https://www.youtube.com/watch?v="

setup=json.loads(sys.argv[1])

profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'en-EN, en')
#profile.set_preference('intl.accept_languages', 'it-IT, it')
driver = webdriver.Firefox(firefox_profile=profile)

#------- carico estensione per bloccare le pubblicità-------#
driver.install_addon("D:\Benny\\università\\Tesi\\extensions\\uBlock0@raymondhill.net.xpi", temporary=False)
driver.get("http://www.youtube.com")
driver.implicitly_wait(5)
password=account_list.get(setup["account"]).get("password")
assert "YouTube" in driver.title

lib.acceptCookies(driver)
#-----Accesso account-------
lib.login(driver,setup['account'],password)
#-----/Accesso account------
#-----Ricerca dei video in home page e visualizzazione del primo consigliato-----


if setup["account"] not in os.listdir("results/"):
    os.mkdir("results/"+setup["account"])


with open("results/"+setup['account']+"/next_exploration.csv","a+",newline='') as session:
   
    watched=lib.getHomeVideosId(driver,session,setup['id'])
    
    print(setup)
    if(setup['query']):
        lib.search(driver,setup['query'])
        lib.getQueryResult(driver,session,setup['id']).click()
    else:
        watched.click()
    #-----/Ricerca dei video in home page e visualizzazione del primo consigliato-----
    while setup['steps']>0:
        
        currentVideoId=driver.current_url[driver.current_url.index("=")+1:]
        length=lib.getDuration(currentVideoId)
        print(length)
        time.sleep(3)
        next_video=lib.getNextVideo(driver,session,currentVideoId,setup['viewTime'],setup['id'])
        
        if length>0:
            if length>setup['viewTime']:
                time.sleep(setup['viewTime'])
            else:
                time.sleep(length-length/4)
            setup['steps']-=1
            next_video.click()
        else:
            setup['steps']-=1
            next_video.click()

assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()

#------Una volta terminati i passi avvio la procedura per inserire i dati relativi ai video nel database-------
lib.setSessionEndTime(setup['id'],setup["startedAtTime"])
print("Id sessione:"+str(setup['id']))
exec(open("fillUpDb.py").read(),{"account":setup['account'],"tipo":2})



from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import lib
import csv
import time
toClick=""
email="emailperlatesi@gmail.com"
password="t3stings3lenium"
base_url="https://www.youtube.com/watch?v="
"""driver = webdriver.Firefox()
driver.get("http://www.youtube.com")
driver.implicitly_wait(5)

assert "YouTube" in driver.title

#-----Accesso account-------
lib.login(driver,email,password)"""
#-----/Accesso account------
#-----Ricerca dei video in home page e visualizzazione del primo consigliato-----
    
#-----/Ricerca dei video in home page e visualizzazione del primo consigliato-----
print (lib.config())
#driver.close()
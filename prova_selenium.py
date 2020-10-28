from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from lib import getDuration
import csv
import time

email="emailperlatesi@gmail.com"
password="t3stings3lenium"

driver = webdriver.Firefox()
driver.get("http://www.youtube.com")

assert "YouTube" in driver.title

time.sleep(2)

elem = driver.find_element_by_id("action-button")

elem.find_element_by_class_name("yt-simple-endpoint").click()

time.sleep(3)

elem=driver.find_element_by_id("identifierId")
elem.send_keys(email)
driver.find_element_by_id("identifierNext").find_element_by_tag_name("button").click()

time.sleep(3)

driver.find_element_by_id("password").find_element_by_tag_name("input").send_keys(password)


driver.find_element_by_id("passwordNext").find_element_by_tag_name("button").click()
time.sleep(3)
videos=driver.find_element_by_id("contents").find_elements_by_id("content")

for element in videos:
    try:
        element.find_element_by_id("overlays")
        element.click()
        break
    except exceptions.NoSuchElementException:
        print("elemento non trovato")
videoId=driver.current_url[driver.current_url.index("=")+1:]
lenght=getDuration(videoId)

next_video=driver.find_element_by_id("related").find_element_by_id("items").find_element_by_id("contents").find_element_by_id("thumbnail").get_attribute("href")
related_videos=driver.find_element_by_id("related").find_element_by_id("items").find_elements_by_id("dismissable")
print(next_video)
with open("session.csv","a+",newline='') as session:
    writer=csv.writer(session)
    writer.writerow([videoId,next_video[next_video.index("=")+1:],1])

    for v in related_videos[1:]:
        relatedVideoId=v.find_element_by_id("thumbnail").get_attribute("href")[v.find_element_by_id("thumbnail").get_attribute("href").index("=")+1:]
        writer.writerow([videoId,relatedVideoId])
        
        print(relatedVideoId)

if lenght>120:
    time.sleep(120)
else:
    time.sleep(lenght-lenght/4)

assert "No results found." not in driver.page_source
time.sleep(5)
#driver.close()



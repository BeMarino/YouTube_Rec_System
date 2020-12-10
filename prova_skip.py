from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import WebDriverWait
password="t3stings3lenium"

base_url="https://www.youtube.com/watch?v="
driver = webdriver.Firefox()
driver.get("http://localhost/Patrimoniale.htm")
driver.implicitly_wait(5)

try: 
    wait = WebDriverWait(driver, 10); 
    element = wait.until(cond.element_to_be_clickable(driver.find_element_by_class_name("ytp-ad-skip-button ytp-button")))
    element.click();  
    
    print("Pubblicita' skippata")
except exceptions.NoSuchElementException:
    print(" no")
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.google.com")

lists_of_webelement = driver.find_elements(By.TAG_NAME, "a")

print(len(lists_of_webelement))

for ele in lists_of_webelement:
    text=ele.text
    href=ele.get_attribute("href")
    print(text)
    print(href)

time.sleep(3)

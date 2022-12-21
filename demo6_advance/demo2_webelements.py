import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.google.com")

lists_of_webelement = driver.find_elements(By.XPATH, "//a")

print(len(lists_of_webelement))

# text = lists_of_webelement[0].text
# print(text)

for i in range(0, len(lists_of_webelement)):
    text = lists_of_webelement[i].text
    print(text)
    href=lists_of_webelement[i].get_attribute("href")
    print(href)

time.sleep(3)

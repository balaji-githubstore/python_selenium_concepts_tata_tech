import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.online.citibank.co.in/")

# check the visibility
# print(driver.find_element(By.XPATH, "//a[@title='Close']").is_displayed())

wait=WebDriverWait(driver,100)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[@title='Close']")))

#check the presence of element
elements = driver.find_elements(By.XPATH, "//a[@title='Close']")
print(len(elements))

#check presence and then click
if len(elements)>0:
    driver.find_element(By.XPATH, "//a[@title='Close']").click()

time.sleep(5)


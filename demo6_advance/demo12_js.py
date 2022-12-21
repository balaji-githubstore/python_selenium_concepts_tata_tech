import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.citibank.co.in/ssjsps/forgetuseridmidssi.jsp")

driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

driver.find_element(By.ID,"citiCard1").send_keys("1234")

#1st approach for date
# driver.find_element(By.ID,"bill-date-long").send_keys("14/04/2000")

#2nd approach for date
# click on date field and check on calendar

#3rd approach for date - javascript
driver.execute_script("document.querySelector('#bill-date-long').value='28/04/2000'")


time.sleep(5)
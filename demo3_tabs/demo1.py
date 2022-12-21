import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.db4free.net/")

#click on phpMyAdmin
# //b[contains(text(),'phpMy')]
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()

lists_of_window= driver.window_handles
print(lists_of_window)
print(lists_of_window[0])
print(lists_of_window[1])
driver.switch_to.window(lists_of_window[1])

driver.find_element(By.ID,"input_username").send_keys("bala")


time.sleep(5)
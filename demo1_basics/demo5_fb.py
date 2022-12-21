import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.facebook.com")


driver.find_element(By.LINK_TEXT,"Create New Account").click()
driver.find_element(By.NAME,"firstname").send_keys("john")


time.sleep(5)
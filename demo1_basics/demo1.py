import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(30)

driver.get("https://demo.openemr.io/b/openemr")

print(driver.title)

print(driver.current_url)

print(driver.page_source)

# driver.find_element(By.LINK_TEXT,"Acknowledgments, Licensing and Certification").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Acknowledgments").click()
time.sleep(5)

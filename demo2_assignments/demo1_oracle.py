import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d= webdriver.Edge()
d.maximize_window()
d.implicitly_wait(30)

d.get("https://www.oracle.com/in/database/")
# time.sleep(5)
#manually click on accept cookies for the time being

d.find_element(By.ID,"acctBtnLabel").click()
d.find_element(By.PARTIAL_LINK_TEXT,"Sign-In").click()

print(d.title)
print(d.current_url)

actual_header=d.find_element(By.XPATH,"//h2").text
print(actual_header)

d.find_element(By.ID,"sso_username").send_keys("john")
d.find_element(By.ID,"ssopassword").send_keys("john")
d.find_element(By.ID,"signin_button").click()
time.sleep(5)
#explicit wait till the visiblity of Invalid error message
actual_error=d.find_element(By.XPATH,"//div[contains(text(),'Invalid')]").text
print(actual_error)


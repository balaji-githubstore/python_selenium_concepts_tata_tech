import time

from selenium import webdriver
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 30,
#                      poll_frequency=1,ignored_exceptions=[NoSuchElementException,StaleElementReferenceException])
wait = WebDriverWait(driver, 30)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")

wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Gmail"))).click()
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Sign in"))).click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, "identifierId"))).send_keys("jack@gmail.com")

alert_text=wait.until(expected_conditions.alert_is_present()).text
wait.until(expected_conditions.alert_is_present()).accept()

time.sleep(5)


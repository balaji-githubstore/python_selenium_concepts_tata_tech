import datetime
import time

from selenium import webdriver, common
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(30)

driver.get("https://nasscom.in/")

print(datetime.datetime.now())
wait = WebDriverWait(driver, 10,poll_frequency=2, ignored_exceptions=[NoAlertPresentException,StaleElementReferenceException,StaleElementReferenceException])
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[text()='Members Listing']")))




# def my_method():
#         def _predicate(_):
#                 try:
#                         # Calling any method forces a staleness check
#                         driver.switch_to.alert
#                         return False
#                 except NoSuchElementException:
#                         return True
#
#         return _predicate
#
# wait = WebDriverWait(driver, 10, ignored_exceptions=[type(common.NoSuchElementException)])
#
# wait.until(my_method())

print(datetime.datetime.now())



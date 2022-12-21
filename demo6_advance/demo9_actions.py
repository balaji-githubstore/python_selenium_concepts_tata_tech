import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://nasscom.in/")

action = webdriver.ActionChains(driver)

action.move_to_element(driver.find_element(By.XPATH, "//a[text()='Membership']"))\
    .move_to_element(driver.find_element(By.XPATH, "//a[text()='Become a Member']"))\
    .perform()

driver.find_element(By.XPATH, "//a[text()='Membership Benefits']").click()

# element=driver.find_element(By.XPATH, "//a[text()='Membership Benefits']")
# driver.execute_script("arguments[0].click()",element)
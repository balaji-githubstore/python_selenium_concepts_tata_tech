import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# switch to frame using name or id as a String

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://netbanking.hdfcbank.com/netbanking/")

driver.switch_to.frame("login_page")
# enter userid as test123
driver.find_element(By.NAME, "fldLoginUserId").send_keys("test123")

driver.find_element(By.LINK_TEXT, "CONTINUE").click()

# switch to main html
driver.switch_to.default_content()

time.sleep(5)

driver.quit()
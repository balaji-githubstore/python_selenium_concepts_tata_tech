import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.db4free.net/")

#click on phpMyAdmin
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()

#switch to 2nd tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID,"input_username").send_keys("admin")
#enter password as admin123
driver.find_element(By.ID,"input_password").send_keys("admin123")
#click on login
driver.find_element(By.ID,"input_go").click()

# actual_error=driver.find_element(By.XPATH,"(//div[@role='alert'])[3]").text.
actual_error=driver.find_element(By.ID,"pma_errors").text
print(actual_error)

#check which tab is getting closed
driver.close()

# switch to 1st tab
driver.switch_to.window(driver.window_handles[0])

print(driver.title)

time.sleep(5)
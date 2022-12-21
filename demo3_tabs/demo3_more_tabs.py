import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.XPATH, "//a[@title='Close']").click()

driver.find_element(By.LINK_TEXT, "APPLY FOR CREDIT CARDS").click()
driver.find_element(By.XPATH, "//span[text()='Login']").click()

# switch using title
for win in driver.window_handles:
    driver.switch_to.window(win)
    print(driver.title)
    if driver.title == "Citibank India":
        break

driver.find_element(By.ID, "User_Id").send_keys("hello")

time.sleep(5)
# will start at 12 PM IST

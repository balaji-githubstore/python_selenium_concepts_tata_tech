import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")

#click on Go
driver.find_element(By.XPATH,"//img[@alt='Go']").click()

#wait for alert to present

wait=WebDriverWait(driver,40)
wait.until(expected_conditions.alert_is_present())

alert_text=driver.switch_to.alert.text
print(alert_text)

driver.switch_to.alert.dismiss()

time.sleep(5)
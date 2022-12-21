import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.ilovepdf.com/pdf_to_word")

# driver.find_element(By.XPATH,"//input[@type='file']").send_keys("D:\\Mine\\balaji-Profile_2022.pdf")

driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"D:\Mine\balaji-Profile_2022.pdf")



time.sleep(5)

driver.quit()
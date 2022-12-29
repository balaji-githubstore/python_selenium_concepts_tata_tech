import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.citibank.co.in/ssjsps/forgetuseridmidssi.jsp")

driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

driver.find_element(By.ID,"citiCard1").send_keys("1234")

#3rd approach for date - javascript

element=driver.find_element(By.XPATH,"//input[@id='bill-date-long']")
driver.execute_script("arguments[0].value='28/04/2000'",element)


# element1=driver.find_element(By.XPATH,"//input[@id='bill-date-long']")
# element2=driver.find_element(By.XPATH,"//input[@id='bill-date-long']")
#
# driver.execute_script("arguments[0].value='28/04/2000'",element1)
# driver.execute_script("arguments[0].value='28/04/2000'",element2)

# element1=driver.find_element(By.XPATH,"//input[@id='bill-date-long']")
# element2=driver.find_element(By.XPATH,"//input[@id='bill-date-long']")
#
# driver.execute_script("arguments[0].value='28/04/2000';arguments[1].value='28/04/2000'",element1,element2)

# https://www.royalcaribbean.com/account/create
# element=driver.find_element(By.XPATH,"//input[@aria-labelledby='emailConsent']")
# driver.execute_script("arguments[0].click()",element)


time.sleep(5)
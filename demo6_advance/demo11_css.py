import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.openemr.io/b/openemr")

driver.find_element(By.CSS_SELECTOR,"#authUser").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys("pass")

select_lan=Select(driver.find_element(By.CSS_SELECTOR,"select[name='languageChoice']"))
select_lan.select_by_visible_text("English (Indian)")

# click on login
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

print(driver.title)

time.sleep(5)
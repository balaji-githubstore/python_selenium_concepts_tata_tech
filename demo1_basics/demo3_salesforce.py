import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME, "UserFirstName").send_keys("john")

# enter lastname as wick
driver.find_element(By.NAME, "UserLastName").send_keys("wick")

# enter email address as john@gmail.com
driver.find_element(By.NAME, "UserEmail").send_keys("john@gmail.com")

# select job title as IT Manager
select_job = Select(driver.find_element(By.NAME, 'UserTitle'))
select_job.select_by_visible_text('IT Manager')

select_country = Select(driver.find_element(By.NAME, 'CompanyCountry'))
select_country.select_by_visible_text('United Kingdom')

driver.find_element(By.XPATH, "//div[@class='checkbox-ui']").click()

time.sleep(5)

driver.quit()

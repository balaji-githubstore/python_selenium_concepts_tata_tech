# will start at 11:45 AM IST
# 1.	Navigate onto  https://www.goto.com/meeting/
# 2.	Click on Accept Recommended Settings
# 3.	Click on Try Free
# 4.	Enter first name as “John”
# 5.	Enter last name as “wick”
# 6.	Enter work email as “john@gmail.com”
# 7.	Company size – 10-99
# 8.	Click on signup
# 9. get password error message


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.goto.com/meeting")

# driver.find_element(By.ID, "truste-consent-button").click()

ele=driver.find_element(By.ID, "truste-consent-button")
ele.click()

# driver.find_element(By.LINK_TEXT,"Try Free").location_once_scrolled_into_view
# time.sleep(3)
driver.find_element(By.LINK_TEXT, "Try Free").click()

driver.find_element(By.ID, "first-name").send_keys("john")

driver.find_element(By.ID, "last-name").send_keys("wick")

driver.find_element(By.ID, "login__email").send_keys("john@gmail.com")

select_count = Select(driver.find_element(By.ID, "CompanySize"))
select_count.select_by_visible_text("10 - 99")

driver.find_element(By.LINK_TEXT, "Terms of Service").location_once_scrolled_into_view
time.sleep(5)
driver.find_element(By.XPATH, "//button[contains(text(),'Start My')]").click()

actual_header = driver.find_element(By.XPATH, "//h1[@class='trial__header']").text
print(actual_header)

actual_password_error = driver.find_element(By.XPATH, "//div[@class='inputField__requirements']").text
print(actual_password_error)

actual_img_src = driver.find_element(By.XPATH, "//img[contains(@src,'ment-alert')]").get_attribute("src")
print(actual_img_src)

# driver.find_element(By.XPATH, "//img[contains(@src,'ment-alert')]").screenshot("image.png")
time.sleep(5)

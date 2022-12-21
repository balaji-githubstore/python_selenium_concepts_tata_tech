from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Software\\chromedriver.exe")

driver.get('https://www.google.com/')
driver.implicitly_wait(30)

print(driver.title)

print(driver.current_url)

# print(driver.page_source)

# driver.find_element(By.PARTIAL_LINK_TEXT,"Gma").click()
print("**********")
actual_text=driver.find_element(By.PARTIAL_LINK_TEXT,"Gma").text
print(actual_text)

actual_tag=driver.find_element(By.PARTIAL_LINK_TEXT,"Gma").tag_name
print(actual_tag)

actual_href=driver.find_element(By.PARTIAL_LINK_TEXT,"Gma").get_attribute("href")
print(actual_href)
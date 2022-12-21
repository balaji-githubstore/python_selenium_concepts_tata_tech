import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
# option.add_argument("--Headless")
# option.set_capability("proxy",option.proxy.httpProxy(""))
# option.binary_location="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

prefs = {"download.default_directory": r"C:\Mine\Company"}
option.add_experimental_option("prefs",prefs)

mobile = {"deviceName": "Pixel 5"}
option.add_experimental_option("mobileEmulation",mobile)


driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.selenium.dev/downloads/")

# driver.find_element(By.PARTIAL_LINK_TEXT,"32").click()

print(driver.title)
time.sleep(5)

import time 
 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Firefox 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.firefox import FirefoxDriverManager

# start by defining the options 
options = webdriver.FirefoxOptions() 
options.headless = True # it's more scalable to work in headless mode 
# normally, selenium waits for all resources to download 
# we don't need it as the page also populated with the running javascript code. 
options.page_load_strategy = 'none' 
# this returns the path web driver downloaded 
firefox_driver = FirefoxDriverManager().install() 
firefox_service = Service(firefox_path) 
# pass the defined options and service objects to initialize the web driver 
driver = Firefox(options=options, service=firefox_service) 
driver.implicitly_wait(5)

url = "https://pogoda.by/weather/numerical-weather-2/26850"
 
driver.get(url) 
time.sleep(5)
content = driver.find_element(By.CSS_SELECTOR, "img[alt*='weather icon'").get_attribute("src")

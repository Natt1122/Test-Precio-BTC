from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service

s= Service("C:/firefox_webdriver/geckodriver.exe")

#Precio del Bitcoin con Web Scraping (Python y Selenium)

#PATH = 'C:/chrome_webdriver/chromedriver.exe'

#driver = webdriver.Chrome(PATH)
driver = webdriver.Firefox(service=s)

driver.get("https://es.investing.com/crypto/bitcoin")

time.sleep(5)

precioBTC = driver.find_element("xpath", '//*[@id="last_last"]')

print('Precio del Bitcoin es : '+ precioBTC.text)

driver.quit()
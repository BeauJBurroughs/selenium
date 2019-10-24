#!/bin/python3

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
url1 = "https://mya.dominionenergy.com
driver.get(url1)
elem = driver.find_element_by_name("USER")
elem.send_keys("#############")                      Dont Forget to change this!
elem = driver.find_element_by_name("PASSWORD")
elem.send_keys("###############")                    Dont forget to change this too!
elem.send_keys(Keys.RETURN)
time.sleep(2)
#Selenium get screenshot
driver.save_screenshot('dom.png')
#Selenium hands the page source to Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

headers = []
values = []
#find headers and values
for header in soup_level1.find_all('h5'):
    headers.append(header)
for value in soup_level1.find_all('p'):
    values.append(value)

print (headers[3].text)
print (values[4].text)
print (values[5].text)

#selenium signout
elem = driver.find_element_by_link_text("Sign Out")
elem.click()
time.sleep(2)
#selenium quit
driver.quit()

#!/bin/python3

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pickle
import json,ast

#import re
#import pandas as pd
#from tabulate import tabulate
#import os

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)
def dom():
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    url= "https://mya.dominionenergy.com"
    driver.get(url)
    elem = driver.find_element_by_name("USER")
    elem.send_keys("##########")                                Dont forget to change this
    elem = driver.find_element_by_name("PASSWORD")
    elem.send_keys("##########")                                Dont forget to change this
    elem.send_keys(Keys.RETURN)
    try:
      element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID, "_MainView1")))
    finally:
      time.sleep(2)
    #Selenium get screenshot
    driver.save_screenshot('../www/dom.png')
    #Selenium hands the page source to Beautiful Soup
    soup_level1=BeautifulSoup(driver.page_source, 'lxml')

    headers = []
    values = []
    #find headers and values
    for header in soup_level1.find_all('h5'):
        headers.append(header)
    for value in soup_level1.find_all('p'):
        values.append(value)

#info=[]
#info.append(headers[3].text)
#print (info)
    info = {"HEADER" : headers[3].text, "DATE" : values[4].text, "AMOUNT" : values[5].text }
#print (headers[3].text)
#print (values[4].text)
#print (values[5].text)

#get cookie and save it (for potential future development no login creds)
    save_cookie(driver,"cookies.pkl")

#selenium signout
    elem = driver.find_element_by_link_text("Sign Out")
    elem.click()
    time.sleep(2)
#selenium quit
    driver.quit()
    with open("dom.json", "w") as write_file:
        json.dump(info, write_file)

dom()

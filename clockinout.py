#!/bin/python

import datetime

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
options.headless = True
desired_caps = DesiredCapabilities.FIREFOX

driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   desired_capabilities=desired_caps,
   options=options)

driver.get('https://clock.payrollservers.us/?wl=payday.payrollservers.us#/clock/web/login')
driver.implicitly_wait(10)

element = driver.find_element_by_id("Username")
element.clear()
element.send_keys("username")
element = driver.find_element_by_id("Password")
element.clear()
element.send_keys("password", Keys.ENTER)
driver.implicitly_wait(10)


#xpath1="//button[@id='ClockIn']"
#clockin = driver.find_element_by_xpath(xpath1)
#clockin.click()

#xpath2="//button[@id='ClockOut']"
#clockout = driver.find_element_by_xpath(xpath2)
#clockout.click()

signout = driver.find_element_by_id("SignOut")
signout.click()



driver.close()

currentDT=datetime.datetime.now()
print("\n\n\n\n\n\n\nClocked IN at " + str(currentDT))
print("\n\n\n\n\n\n\nClocked OUT at " + str(currentDT))  

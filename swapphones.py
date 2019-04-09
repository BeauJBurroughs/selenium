#!/bin/python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


EXT1 = input("what is your EXT#?")
EXT2 = input("what is the EXT# you want to swap?")

#to run headless
options = Options()
options.headless = True
desired_caps = DesiredCapabilities.FIREFOX

driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   desired_capabilities=desired_caps,
   options=options)

driver.get("http://10.40.0.51")
driver.switch_to_frame("mainFrm")
element = driver.find_element_by_name("userName")
element.send_keys("ADMIN2")
element = driver.find_element_by_name("password")
element.send_keys("9999", Keys.ENTER)
driver.implicitly_wait(10)


swap_link = driver.find_element_by_link_text("Swap")
swap_link.click()

xpath1="//option[@value='" + str(EXT1) + "']"
swap1 = driver.find_element_by_xpath(xpath1)
swap1.click()

xpath2="(//option[@value='" + str(EXT2) + "'])[2]"
swap2 = driver.find_element_by_xpath(xpath2)
swap2.click()

apply_link = driver.find_element_by_link_text('Apply')
apply_link.click()

home_link = driver.find_element_by_link_text('Home')
home_link.click()

logout_link = driver.find_element_by_link_text('Logout')
logout_link.click()

driver.close()


print ("\n\n\n\n\n\n\nPhones successfully swapped")

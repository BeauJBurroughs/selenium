from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
driver.get("<SOPHOS_ROUTER_IPADDRESS")                                               #IPADDRESS
elem = driver.find_element_by_id("username")
elem.send_keys("<USERNAME>")                                                         #USERNAME
elem = driver.find_element_by_id("password")
elem.send_keys("<PASSWORD>")                                                         #PASSWORD
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
elem = driver.find_element_by_name("button")
elem.click()
time.sleep(5)
driver.implicitly_wait(10)
Firewall = driver.find_element_by_link_text("Firewall")
hover = ActionChains(driver).move_to_element(Firewall)
hover.click(Firewall).perform()
driver.implicitly_wait(10)
elem = driver.find_element_by_link_text("<NAME OF FIREWALLRULE...>")                 #FIREWALLRULE
elem.click()
driver.implicitly_wait(10)

#_______________________________________________________________________________________________________________

body = driver.find_element_by_xpath('/html/body')
body.click()
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(10)

Policy = driver.find_element_by_xpath("//span[contains(.,'<FAILOVER_POLICY>')]")     #failover (currently selected)
#Policy = driver.find_element_by_xpath("//span[contains(.,'<FALLBACKTO_POLICY>')]")  #fallback
hover = ActionChains(driver).move_to_element(Policy)
hover.click(Policy).perform()
driver.implicitly_wait(10)

#elem = driver.find_element_by_xpath("//span[contains(.,'<FAILOVER_POLICY>')]")      #fallback 
elem = driver.find_element_by_xpath("//span[contains(.,'<FALLBACKTO_POLICY>')]")     #failover (currently selected)
elem.click()

elem = driver.find_element_by_id("btnOK")
elem.click()
driver.implicitly_wait(10)
time.sleep(5)

logout = driver.find_element_by_xpath("//span[contains(.,'admin')]")
hover = ActionChains(driver).move_to_element(logout)
hover.click(logout).perform()
driver.implicitly_wait(10)

elem = driver.find_element_by_link_text("Logout")
elem.click()

driver.close()
driver.quit()

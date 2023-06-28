from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#how to handle mouse actions-
#using ActionChains class, create an object of the class and use the methods

action=ActionChains(driver)#pass driver as the argument
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()#for actions we need to end with perform method
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

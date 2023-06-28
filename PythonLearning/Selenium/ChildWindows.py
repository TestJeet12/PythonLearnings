from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
#how to handle multi tab windows
driver.find_element(By.LINK_TEXT,"Click Here").click()
windows=driver.window_handles#this will help us store the opened windows in the variable as a list
driver.switch_to.window(windows[1])#passinh windows[1] as argument as its second window and list index starts with 0
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(windows[0])#switching back to parent window
assert "Opening a new window"==driver.find_element(By.TAG_NAME,"h3").text
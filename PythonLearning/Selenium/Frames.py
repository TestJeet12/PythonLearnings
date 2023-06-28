from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
#how to handle frames - frames are embedded on top of the local HTML
#hence we need to switch to frames like windows tabs, we have iframe tag in the HTML

driver.switch_to.frame("mce_0_ifr")#argument can be name or ID attribute under iframe tag
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Iam able to automate frames")
driver.switch_to.default_content()#to switch back to local HTML
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
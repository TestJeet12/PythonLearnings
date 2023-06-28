from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)

driver.get("https://www.rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()#link text we can use if anchor a tag is present
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")#traversing from parent to child
#using xpath
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("123456")
#traversing from parent to child
#using css
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("123456")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()#xpath using text attribute, using text
#on the element.
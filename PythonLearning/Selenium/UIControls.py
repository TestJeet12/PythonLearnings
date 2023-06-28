import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
#here we will see how to click on the checkboxes and radio buttons
#below type of code writing we will use when we are not sure if the checkbox will stay in the same location
#like if the option2 checkbox is moving up or down, hence we used for loop
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":# we are using getattribute as we have the attribute inside the tag
        checkbox.click()
        assert checkbox.is_selected()# this method .isselected will be used to check whether checkbox is selected or not
        break

#now we will do the same for radio buttons
radiobuttons=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
radiobuttons[2].click()
time.sleep(10)

#now we will see the other asserts
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

#handling java alerts-
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert#this will switch the control from the browser window to the java alert
alerttext=alert.text
print(alerttext)
alert.accept()


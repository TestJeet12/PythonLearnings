from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(4)#always try to ass this global wait before the get method

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()#here in this xpath locator we are using
#regular expressions meaning part of the attribute value, similar for CSS syntax is
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
#now we have to select blackberry product
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productname=product.find_element(By.XPATH,"div/h4").text
    if productname=="Blackberry":
        product.find_element(By.XPATH,"div/button").click()#here if u inspect and check we have not used div[2]
    #because xpath will check the button if its not present inside the first div then automatically second div will be
    #selected , but if button is present in both the divs then we have to specify div[2]
        break
driver.find_element(By.CSS_SELECTOR,"a[class*='btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()#we can use css or xpath without tag name as well
#xpath ex-//*[@type='submit']
Successmessage=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in Successmessage#this is partial assertion



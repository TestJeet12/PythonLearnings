import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(5)
#implicit wait is the global wait which will wait till the element is not found on the browser
#explicit wait is for the particular locator element where generally it might take some time than usual
#explicit wait is to be used for findelements as otherwise test case will pass with empty list

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()


expectedlist=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actuallist=[]
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")



#now we have to validate the list contains the correct products or not-
time.sleep(5)
wait=WebDriverWait(driver,15)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='products']/div")))
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
print(count)
assert count==3
for result in results:
    actuallist.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()#this is called chaining, till result we have
    #xpath for all the elements and once in for loop we find the required one or for every loop element we can
    #just chain the remaining components
assert expectedlist==actuallist

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()#text only in xpath
#sum of prices on checkout page validation
prices=driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalamount


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#wait is the object of WebDriverWait class
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
discountedamount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalamount>discountedamount



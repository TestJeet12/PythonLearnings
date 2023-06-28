from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#here we will see how to check the sorting on the site is working fine or not
#Step1-click on the column header to sort the table on browser
driver.find_element(By.XPATH,"//tr/th[1]").click()


#Step2-collect all the veggies/fruits name and store in a list (variable 1)and now copy it into a new
# list(variable 2)
variable1=[]
veggiesfruits=driver.find_elements(By.XPATH,"//tr/td[1]")
for veg in veggiesfruits:
    variable1.append(veg.text)
variable2=variable1.copy()#we can use slice method also to copy
#Step3-sort the list (variable 1)
variable1.sort()
#Step4-compare the original list with the sorted list (variable 1 with variable 2)
assert variable1==variable2

#just a note- to debug use a breaking point on the line number and click on the bug icon, we can control and see
#step by step execution of the scripts in the console

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
#here we will see how to handle dynamic dropdowns
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
#now we have to collect the elements in a list using find elements
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
print(len(countries))# to check the List length
#now go through the list using for loop
for country in countries:
    if country.text=="India":
        country.click()#here country will store element for each loop through the list
        break
#now we need to check whether correct value "India" is selected or not-
assert driver.find_element(By.ID,"autosuggest").get_attribute("value")== "India"#here we are using getattribute
#method as .text will only work for the values present on first browser load , and India value is selected through script


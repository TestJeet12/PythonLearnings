from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)

#to find the elements on the web page we use different locators-xpath, css, id, linktext, partiallinktext,
#classname,name etc, all the things depends on the attributes defined on by the developer except
#css and xpath , we can construct locators for any element using css and xpath.
#id is mostly unique

# add Selectors hub plugin to chrome to validate the xpath and css selectors

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("test@gmail.com")#send keys is to input value
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

#xpath syntax- //tagname[@attribute='value']
#css syntax- tagname[attribute='value'], #Id, .classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Jeet")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
#static dropdown selection-
#whenever we have a select tag in the inspect we can use Select class
#first create a object of Select class

dropdown=Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
#dropdown will store the element
dropdown.select_by_index(0)
#dropdown.select_by_value() # we cannot select by value as value attribute is not present inside the tag
dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
#text is to capture and store the text on the element
#if the class name is having spaces then it means it has multiple classes and we can use anyone
print(message)
assert "Success" in message#to validate the message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Test again")#see the locator, this
#is an example of selecting from multiple options, type= text is matching with 3 elements , we know third one is
#correct hence third one we mentioned
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()# to clear the values on the element



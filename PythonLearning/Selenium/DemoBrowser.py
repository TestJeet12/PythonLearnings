#to launch the browser we need to call the webdriver class which is in the selenium package
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#to invoke the chrome browser we need to invoke the proxy driver of chrome which will invoke the chrome browser
#first we need to create object of class Service which will store the active data and location of the chrome driver
#now we need to create the object driver for the webdriver class and pass the service object as argument
Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
driver.maximize_window()#to maximize the window
driver.get("https://rahulshettyacademy.com/")
driver.minimize_window()#to minimize the window
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.back()# to go back
driver.refresh()#to refresh the page
driver.forward()#to go forward
print(driver.title)#to ge the tab name
print(driver.current_url)#to ge the current URL
driver.close()#to close the browser

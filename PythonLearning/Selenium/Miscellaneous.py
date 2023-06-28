from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#chromeoptions- this is a class present in the webdriver package
#it has some methods we can use to define somethings and if we want to do some with the browser before it
#triggers through script like opening in headless mode , meaning backend window will open frontend we cannot see the execution
#first create a object of chromeoptions class
chromeoptions=webdriver.ChromeOptions()
#chromeoptions.add_argument("headless")#to open the browser in headless mode
chromeoptions.add_argument("--ignore-certificate-errors")#it will ignore the errors ,sometimes we see some SSL certificate errors those
chromeoptions.add_argument("--start-maximized")#broser window will be maximized everytime for the execution
#arguments for the add_argument we can find in net
#now pass the chromeoptions in the chrome class line-16
Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj,options=chromeoptions)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.maximize_window()

#here we will see java script executor
#some events we cannot persom directly like scrolling the window for that we need to execute
#java script using selenium on the browser
#first get the script - inspect the page and click on console and try the script then pass it as
#argument in the execute_script method
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")#to take the screenshot


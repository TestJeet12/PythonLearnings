

from selenium.webdriver.common.by import By

from Pageobjects.Checkoutpage import CheckOutPage

#illustration of the page object design
#create a class and define variables which will store the web elements
#now create different methods which has the functionality of finding the elements

class HomePage:

    #defined a constructor so when a object is created for this class that time we will pass the driver
    #object which will be used here in this class
    #in constructor we will define the local driver with the driver we get while creating the object
    #of this class
    def __init__(self , driver):
        self.driver=driver


    shop=(By.CSS_SELECTOR, "a[href*='shop']")#this is a tuple
    #productlist=(By.XPATH, "//div[@class='card h-100']")
    productlist=(By.CSS_SELECTOR, ".card-title a")
    #productname=(By.XPATH, "div/h4")
    productname=(By.CSS_SELECTOR, ".card-title a")
    #product=(By.XPATH,"div/button")
    product=(By.CSS_SELECTOR, ".card-footer button")
    checkout=(By.CSS_SELECTOR, "a[class*='btn btn-primary']")


    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")


    def shopbutton(self):
        return self.driver.find_element(*HomePage.shop)#in the argument u can see * , this is to deserialize the tuple

    def productslist(self):
        return self.driver.find_elements(*HomePage.productlist)

    #def productnamem(self):
        #return self.driver.find_elements(*HomePage.productname)


    def productm(self):
        return self.driver.find_elements(*HomePage.product)


    #observe the below method-
    #here we have in first line we are performing the click operation and in the second line
    #we are creating a object of another page object class , as we know the first operation will
    #result in next page hence instead of creating object separately in the test class for the next page
    #we will execute this method and catch the object in main test file
    def checkoutbutton(self):
        self.driver.find_element(*HomePage.checkout).click()
        checkoutpages = CheckOutPage(self.driver)#passing self.driver as argument which is this class
        #driver sent to checkoutpage class constructor
        return checkoutpages



    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)











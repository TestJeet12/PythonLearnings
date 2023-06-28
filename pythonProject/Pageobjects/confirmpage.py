from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver=driver

    location=(By.ID, "country")
    country=(By.LINK_TEXT, "India")
    checkbox=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitbutton=(By.CSS_SELECTOR,"[type='submit']")
    successmsg=(By.CLASS_NAME, "alert-success")

    def locationclick(self):
        return self.driver.find_element(*ConfirmPage.location)

    def countryclick(self):
        return self.driver.find_element(*ConfirmPage.country)

    def checkboxclick(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def submitbuttonclick(self):
        return self.driver.find_element(*ConfirmPage.submitbutton)

    def successmsgm(self):
        return self.driver.find_element(*ConfirmPage.successmsg)








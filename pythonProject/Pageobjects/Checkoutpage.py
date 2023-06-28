from selenium.webdriver.common.by import By

from Pageobjects.confirmpage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver



    checkoutbuttondata=(By.XPATH, "//button[@class='btn btn-success']")

    def checkoutbuttonn(self):
        self.driver.find_element(*CheckOutPage.checkoutbuttondata).click()
        confirmpage=ConfirmPage(self.driver)
        return confirmpage

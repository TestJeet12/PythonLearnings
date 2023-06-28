from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


import pytest

from Pageobjects.HomePage import HomePage
#from Pageobjects.HomePage import HomePage
from Utilities.Baselass import Baseclass


class Testone(Baseclass):#make a habit of wrapping all the test cases methods under class
    #here we are inheriting the Baseclass.


    def test_e2e(self, setup):#setup we passed as argument as setup method is returing the driver object
        log = self.getLogger()
        homepage=HomePage(self.driver)



        self.driver.implicitly_wait(4)  # always try to ass this global wait before the get method
        # driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()#here in this xpath locator we are using
        # regular expressions meaning part of the attribute value, similar for CSS syntax is
        homepage.shopbutton().click()
        # now we have to select blackberry product
        products = homepage.productslist()
        i = -1
        for product in products:
            i = i+1
            productname = product.text
            if productname == "Blackberry":
                homepage.productm()[i].click()  # here if u inspect and check we have not used div[2]
                # because xpath will check the button if its not present inside the first div then automatically second div will be
                # selected , but if button is present in both the divs then we have to specify div[2]
                break
        checkoutpages= homepage.checkoutbutton()
        confirmpages=checkoutpages.checkoutbuttonn()
        confirmpages.locationclick().send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        confirmpages.countryclick().click()
        confirmpages.checkboxclick().click()
        confirmpages.submitbuttonclick().click()  # we can use css or xpath without tag name as well
        # xpath ex-//*[@type='submit']
        Successmessage = confirmpages.successmsgm().text
        assert "Success! Thank you!" in Successmessage  # this is partial assertion
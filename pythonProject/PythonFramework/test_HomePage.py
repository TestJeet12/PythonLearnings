from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from Testdata.HomePageData import HomePageData
from Pageobjects.HomePage import HomePage
from Utilities.Baselass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    #this fixture we are keeping here coz its specific to this test class only
    #and the data is coming from the homepagedata class
    #note- any class things we can call using the classname.method/variablename
    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param
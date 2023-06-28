import pytest
driver=None#defining global driver as none initially when the fixture setup is executed then there this
#global variable is defined with the local driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#if we want to select browser where to run the test scripts we need to pass the options at runtime
#for that we will use the below piece of code called hook in python, we can find in the
#net here -https://docs.pytest.org/en/7.1.x/example/simple.html
#command line syntax- py.test --browsername chrome
def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome"
    )


@pytest.fixture(scope="class")

def setup(request):
    global driver#pointing to the driver on top(global driver)
    browsername=request.config.getoption("--browsername")#here we are capturing and storing the
    #the browser name passed in run time , this also we can get in https://docs.pytest.org/en/7.1.x/example/simple.html
    #now we have the browser name from runtime now we can write ifelse statements to chose the browser
    #which user has mentioned at runtime.
    if browsername=="Chrome":
        Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=Service_obj)
    elif browsername=="IE":
        Service_obj = Service("C:/Users/RA553LM/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=Service_obj)

    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver#as we know request is the instance of the fixture
    #so cls.driver is the driver variable of the class where we are calling the fixture which will
    #hold the driver object from this method and in the test class where we are calling the fixture
    #we can use self.driver and work.
    #note- we are not using return driver as we are using tear down code yield , hence we cannot use
    #return statement here , as it should be the last line(mb)
    yield
    driver.close()

#this below complete fixture is available in net for taking screenshots on failure
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

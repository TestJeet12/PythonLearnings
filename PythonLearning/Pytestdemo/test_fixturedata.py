import pytest

from Pytestdemo.Baseclass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):#inheritance as we want to use logger here

    def test_dataload(self,dataload):#if the fixture is returning something then fixture name should be passed as the argument
        log=self.getLogger()
        log.debug("Test debug")
        log.info(dataload[1])
        print(dataload)
        print(dataload[1])

#to generate html report then install pytest_html from cmd using pip install pytest-html
#to generate html report use flag --html=reportname.html
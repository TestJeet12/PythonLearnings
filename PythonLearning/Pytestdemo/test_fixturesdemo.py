import pytest


@pytest.mark.usefixtures("setup")#this is used if we need fixture for all the methods of the below class
class Testexample:

    def test_fixture1(self):#parameter self has to be passed if the method is defined under a class
        print("fixture1")
    def test_fixture2(self):
        print("fixture2")


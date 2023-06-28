#imp points for Pytest framework
#first open cmd and install- pytest with command- pip install pytest
#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#any code should be wrapped in method only
#Method name should have sense
#py.test is the command to run all the tests
#-k stands for method names execution (specific method names - regular expressions),-s flag is for logs
#in output, -v stands for more information metadata
#you can run specific file with py.test<filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m flag
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail - we use this when we expect any failure but we still want to partially run it without reporting the error
#fixtures are used as setup and tear down methods for test cases- conftest file to generalise
#fixtures and make it available to all test cases(fixture name into parameters of methods)
#data driven and parameterization can be done with return statements in tuple format
#when u define fixture scope to class only, it will run once before  class execution is initiated and once class is completed
import pytest


@pytest.mark.smoke
def test_firstmethod():
    print("Hello")


def test_secondmethod():
    print("GM")

#@pytest.fixture()#defining a fixture , suppose we want to execute a method before some method then we use this
#its like we have to open a browser then we can execute so opening the browser details we keep in fixture- just an example

#def setup():
    #print("executing first")
    #yield#when we use yield then whatever the statements are present after the field those will be
    #executing at last, like before yield statements, then the method where fixture is passed as arguments and then after yield statements

    #print("executing last")
def test_fixturedemo(setup2):#passing the fixture name as argument, observe the execution
    print("executing method")


#to run the pytest files from pycharm, next to run icon , click -edit configurations-+-pytests-u can give file path as well
#for specific file to run

#if two method names are same in the file then python will overwrite the output with the latest one only











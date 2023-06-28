import pytest

#this conftest files we can define fixtures , only when this fixtures is required by multiple test files
@pytest.fixture(scope="class")#scope = class ,now where ever this fixture is called there fixture will not be
    #executed for all the methods of the class instead it will execute once the class starts and then the methods
    #of the class and when the methods execution is done yield statements are executed
def setup():
    print("executing first")
    yield
    print("executing last")

@pytest.fixture()
def setup2():
    print("executing first setup 2")
    yield
    print("executing last set up 2")

@pytest.fixture()
def dataload():
    print("Dataloading")
    return ["A","B","C","D"]

@pytest.fixture(params=[("A","B"),("C","D")])#this is when we need to pass some data in every run, in this case
    #A,B will be passed in first run and C,D is passed in second run
    #classic example is when we invoke multiple browsers then we need to set data in multiple browsers etc
def crossbrowser(request):#request is an instance/object of the fixture
    return request.param
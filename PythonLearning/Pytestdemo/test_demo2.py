import pytest


@pytest.mark.smoke#this is a mark for smoke test
def test_demo2firstmethod():
    print("Hello")

@pytest.mark.skip#this mark will skip the below test method
def test_demo2secondmethod():
    msg="Hello"
    assert msg=="Hi","not matching error" #after the comma whatever is there will be displayed only if the
    #assertion fails

def test_fixtureparameter(crossbrowser):
    print(crossbrowser[1])
    print("parameter fixture")

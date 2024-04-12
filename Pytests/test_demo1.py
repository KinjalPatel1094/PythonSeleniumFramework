# pytests always start with test_ or end with _test.
# method names always start with test.
# Any code should be wrapped in method only in pytest framework.
# Method name should have sense.
# -k stands for method name execution , -s stands for logs in output, -v stands for more info metadata.
# you can run specific file using py.test <<file name>>
# You can mark tests for smoke , regression and run only those tests using -m <test type>
# If you want to ignore error message in terminal , but still want some operations required from that test ,
# use "xfail" mark!

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("First Pytest")


@pytest.mark.xfail
def test_greetPractice():
    print("Good morning")
    a = 100 / 2
    assert a == 40, "value did not match , incorrect"


# returning data from fixture declared in conftest file.
def test_browser_data(browser_data):
    print(browser_data)
    print(browser_data[1])
    print(browser_data[0])

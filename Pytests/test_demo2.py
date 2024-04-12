# If there is any testcase that is failing , you can skip it by marking skip and run all other tests.


import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == "hi", "this test fails as strings do not match"


def test_secondProgramPractice():
    a = 4
    b = 2
    assert a+b == 6, "addition do not match"


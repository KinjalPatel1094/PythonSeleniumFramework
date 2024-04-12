# This is a fixture file , name should be given this only to define fixture separately for all tests!
# Fixtures are used as setup and teardown methods for testcase files.
# conftest file is to generalize fixture and make it available to all tests.

import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def data_load():
    print("User profile data is being created")
    return ["kinjal", "patel", "kinjal@test.com"]


@pytest.fixture(params=[("Chrome", "main Browser"), ("Firefox", "Second Browser"), "IE"])
def browser_data(request):
    return request.param  # Returning single parameter each time , so param and not params here.

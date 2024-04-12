# When you want your test to return values from fixtures ,
# you need to declare fixture name globally and as a parameter in that test.
# When declaring at class level , you need to use @pytest.mark.fixtures().
# At method level , it is not required. Just pass the fixture as parameter.

import pytest


@pytest.mark.usefixtures("data_load")
class TestExample2:

    def test_editProfile(self, data_load):
        print(data_load)
        print(data_load[0])
        print(data_load[1])
        print(data_load[2])

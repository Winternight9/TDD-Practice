import pytest
from leap_year import is_a_leap_year

class TestLeapYear:

    def test_2100_is_not_a_leap_year(self):
        assert is_a_leap_year(2100) == False

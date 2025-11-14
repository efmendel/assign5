import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import Location, UserProfile  # Import both from src

user1 = UserProfile(
    name="Steph Curry",
    email="scurry@gmail.com",
    password="Apoisjfp1@",
    dob="05/20/2006",
    location=Location(city="SanFrancisco", state="CA", country="US"),
)
user2 = UserProfile(
    name="James Harden",
    email="jharden@gmail.com",
    password="Apoisjfp@1",
    dob="08/26/1989",
    location=Location(city="Houston", state="TX", country="US"),
)

user3 = UserProfile(
    name="Michael Jordan",
    email="mjordan@gmail.com",
    password="A@poisjfp1",
    dob="1963-02-17",
    location=Location(city="Chicago", state="IL", country="US"),
)

user4 = UserProfile(
    name="Kevin Durant",
    email="kdurant@gmail.com",
    password="@A1poisjfp",
    dob="09/09/1988",
    location=Location(city="Phoenix", state="AZ", country="US"),
)

user5 = UserProfile(
    name="Lebron James",
    email="lbjames@gmail.com",
    password="A1poisjfp@",
    dob="11/13/1984",
    location=Location(city="LosAngeles", state="CA", country="US"),
)

user6 = UserProfile(
    name="Kobe Bryant",
    email="kbryant@gmail.com",
    password="aPoisjfp1@",
    dob="11/14/1978",
    location=Location(city="LosAngeles", state="CA", country="US"),
)

user7 = UserProfile(
    name="Giannis Antetokounmpo",
    email="gantetokounmpo@gmail.com",
    password="a1Poisjfp@",
    dob="11/12/1994",
    location=Location(city="Milwaukee", state="WI", country="US"),
)

user8 = UserProfile(
    name="Luka Doncic",
    email="ldoncic@gmail.com",
    password="1aPoisjfp@",
    dob="11/02/1999",
    location=Location(city="Dallas", state="TX", country="US"),
)


class TestUserAge:
    # order: upper lower digit special
    def test_password_upper_lower_digit_special(self):
        assert user1.validate() == True

    # order: upper lower special digit
    def test_password_upper_lower_special_digit(self):
        assert user2.validate() == True

    # order: upper special lower digit
    def test_password_upper_special_lower_digit(self):
        assert user3.validate() == True

    # order: special upper digit lower
    def test_password_special_upper_digit_lower(self):
        assert user4.validate() == True

    # order: upper digit lower special
    def test_password_upper_digit_lower_special(self):
        assert user5.validate() == True

    # order: lower upper digit special
    def test_password_lower_upper_digit_special(self):
        assert user6.validate() == True

    # order: lower digit upper special
    def test_password_lower_digit_upper_special(self):
        assert user7.validate() == True

    # order: digit lower upper special
    def test_password_digit_lower_upper_special(self):
        assert user8.validate() == True

    # fails when it doesn't start with uppercase --> regex needs to be checked

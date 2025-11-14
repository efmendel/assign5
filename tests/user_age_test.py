import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

user1 = UserProfile(
    name="Steph Curry",
    email="scurry@gmail.com",
    password="Bigsteph123!",
    dob="05/20/2006",
    location={"city": "San Francisco", "state": "California", "country": "US"},
)
user2 = UserProfile(
    name="James Harden",
    email="jharden@gmail.com",
    password="TheBeard13!",
    dob="08/26/1989",
    location={"city": "Houston", "state": "Texas", "country": "US"},
)

user3 = UserProfile(
    name="Michael Jordan",
    email="mjordan@gmail.com",
    password="Airness23!",
    dob="1963-02-17",
    location={"city": "Chicago", "state": "Illinois", "country": "US"},
)

user4 = UserProfile(
    name="Kevin Durant",
    email="kdurant@gmail.com",
    password="SlimReaper35!",
    dob="09/09/1988",
    location={"city": "Phoenix", "state": "Arizona", "country": "US"},
)

user5 = UserProfile(
    name="LeBron James",
    email="lbjames@gmail.com",
    password="KingJames23!",
    dob="11/13/1984",
    location={"city": "Los Angeles", "state": "California", "country": "US"},
)

user6 = UserProfile(
    name="Kobe Bryant",
    email="kbryant@gmail.com",
    password="BlackMamba24!",
    dob="11/14/1978",
    location={"city": "Los Angeles", "state": "California", "country": "US"},
)

user7 = UserProfile(
    name="Giannis Antetokounmpo",
    email="gantetokounmpo@gmail.com",
    password="GreekFreak34!",
    dob="11/12/1994",
    location={"city": "Milwaukee", "state": "Wisconsin", "country": "US"},
)

user8 = UserProfile(
    name="Luka Doncic",
    email="ldoncic@gmail.com",
    password="LukaMagic77!",
    dob="11/02/1999",
    location={"city": "Dallas", "state": "Texas", "country": "US"},
)


class TestUserAge:
    # standard case
    def test_valid_age(self):
        assert user1.get_age() == 19

    # pre 2000
    def test_pre_2000_age(self):
        assert user2.get_age() == 36

    # different format
    def test_other_dob_format(self):
        assert user3.get_age() == 62

    # test same day and month
    def test_same_month_day_dob(self):
        assert user4.get_age() == 37

    # test birthday today
    def test_birthday_today(self):
        assert user5.get_age() == 41

    # test birthday tomorrow
    def test_birthday_tomorrow(self):
        assert user6.get_age() == 46

    # test birthday yesterday
    def test_birthday_yesterday(self):
        assert user7.get_age() == 31

    # test birthday earlier in the same month
    def test_birthday_earlier(self):
        assert user8.get_age() == 26

    # bug: misjudges age when its the month of their birthday and their bithday already happened

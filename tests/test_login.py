import pytest

from pages.login_page import LoginPage
from utils.capabilities import create_ios_driver
from utils.csv_util import read_csv

test_data = read_csv("data/login_data.csv")
print(test_data)

@pytest.mark.parametrize("data",test_data)
def test_valid_login(driver,data):
    login_page = LoginPage(driver)
    username=data["username"]
    password=data["password"]
    expected=data["expected"]
    #login_page.login("standard_user", "secret_sauce")
    login_page.login(username,password)
    assert False ,"Forced failure to test screenshot attachment"


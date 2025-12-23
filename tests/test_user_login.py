import time

import pytest

from src.pages.base_page import Dashboard
from src.pages.login_page import Login
from src.utils.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestLogin:

    baseUrl = ReadConfig.get_application_url()
    mobile_number = ReadConfig.get_user_mobile()
    password = ReadConfig.get_user_password()

    def test_user_login(self, setup):
        driver = setup
        driver.get(self.baseUrl)

        dashboard = Dashboard(driver)
        time.sleep(2)
        dashboard.click_language_icon()
        time.sleep(3)
        dashboard.click_english_option()
        time.sleep(3)
        dashboard.click_signin_button()
        time.sleep(3)

        login = Login(driver)
        login.change_country()
        time.sleep(3)
        login.select_country_india()
        time.sleep(2)
        login.set_mobile_number(self.mobile_number)
        time.sleep(2)
        login.set_password(self.password)
        time.sleep(2)
        login.click_login()
        time.sleep(3)



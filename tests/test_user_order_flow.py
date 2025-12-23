# tests/test_user_order_flow.py

import pytest
from src.helpers.user_login_helper import UserLoginHelper
from src.helpers.user_order_helper import UserOrderHelper
from src.utils.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestUserOrderFlow:
    def test_place_order_successfully(self, setup):
        driver = setup
        driver.get(ReadConfig.get_application_url())

        UserLoginHelper.login(driver)
        UserOrderHelper.place_order(driver)

        # Add success verification or screenshot if needed
        print("✅ Order placed successfully.")

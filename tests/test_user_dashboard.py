import time

import pytest
from src.helpers.user_login_helper import UserLoginHelper


@pytest.mark.usefixtures("setup")
class TestUserDashboard:

    def test_open_dashboard_after_login(self, setup):
        driver = setup
        UserLoginHelper.login(driver)
        time.sleep(4)

        # Now user is logged in, you can test anything here
        assert "renter/companies" in driver.current_url
        print("✅ Dashboard opened after login")
        driver.close()

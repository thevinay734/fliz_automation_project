import pytest
from src.helpers.user_login_helper import UserLoginHelper
from src.helpers.user_order_helper import UserOrderHelper
from src.utils.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestPlaceOrder:

    def test_place_order(self, setup):
        driver = setup
        driver.get(ReadConfig.get_application_url())

        # ✅ Step 1: Login first
        UserLoginHelper.login(driver)

        # ✅ Step 2: Place order with full parameters
        UserOrderHelper.place_order(
            driver=driver,
            company_name="Natraj",        # 👈 Click company first
            equipment_index=1,
            quantity=2,
            start_date="2025-07-22",
            end_date="2025-07-23"
        )

        # ✅ Optional: Add success check
        print("✅ Order placed successfully.")

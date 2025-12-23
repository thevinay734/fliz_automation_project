import time

from src.pages.base_page import Dashboard
from src.pages.login_page import Login
from src.utils.readproperties import ReadConfig


class UserLoginHelper:

    @staticmethod
    def login(driver):
        base_url = ReadConfig.get_application_url()
        user_mobile = ReadConfig.get_user_mobile()
        user_password = ReadConfig.get_user_password()

        print(f"Attempting to login to: {base_url}")
        print(f"Using mobile number: {user_mobile}")
        print(f"Using password: {user_password}")

        # Step 1: Open site and change language
        driver.get(base_url)
        dashboard = Dashboard(driver)
        dashboard.wait_for_page_to_load()
        dashboard.click_language_icon()
        dashboard.click_english_option()
        dashboard.click_signin_button()
        time.sleep(5)

        # Step 2: Login process
        login = Login(driver)

        login.change_country()
        login.select_country_india()
        login.set_mobile_number(user_mobile)
        login.set_password(user_password)
        login.click_login()

        # Step 3: Verify login success
        assert "/en/" in driver.current_url, f"Expected '/en/' in URL but got: {driver.current_url}"
        print("✅ User login successful")

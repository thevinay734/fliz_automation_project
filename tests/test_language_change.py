import time

import pytest
from src.pages.base_page import Dashboard
from src.utils.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestLanguageChange:

    baseUrl = ReadConfig.get_application_url()

    def test_change_language_arabic_to_english(self, setup):
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


        # ✅ Verify URL changed
        assert "/en/" in driver.current_url, f"Expected '/en/' in URL but got: {driver.current_url}"
        print("✅ Language changed to English successfully.")
        driver.close()






import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators.locators import DashboardLocators


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_equipment_category(self, *category_names):
        for name in category_names:
            print(f"🔍 Trying to select equipment category: {name}")
            locator = DashboardLocators.CATEGORY_BY_TEXT(name)
            try:
                self.wait.until(EC.presence_of_element_located(locator))
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                print(f"✅ Successfully clicked: {name}")
                time.sleep(1)
            except TimeoutException:
                raise Exception(f"[❌] Could not find or click element with text '{name}'")

    def click_company(self, company_name):
        print(f" Trying to click company: {company_name}")
        locator = DashboardLocators.COMPANY_BY_NAME(company_name)
        try:
            company_element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", company_element)
            company_element.click()
            print(f"✅ Clicked company: {company_name}")
            time.sleep(2)
        except TimeoutException:
            raise Exception(f"❌ Could not find or click company '{company_name}'")

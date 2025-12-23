from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.locators.locators import ServiceDetailsLocators


class ServiceDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def set_quantity(self, quantity):
        print(f"🔢 Setting quantity to: {quantity}")
        for _ in range(quantity - 1):
            plus_button = self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.PLUS_BUTTON))
            plus_button.click()

    def select_start_date(self, day):
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Start Date')]").click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class,'react-datepicker__day--0{day[-2:]}')]").click()

    def select_start_date(self, date_label):
        print("⏳ Waiting for Start Date field...")
        self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.START_DATE_FIELD)).click()
        print("✅ Clicked Start Date box")
        self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.DATE_PICKER_DAY_BY_LABEL(date_label))).click()
        print(f"✅ Selected Start Date: {date_label}")

    def select_end_date(self, date_label):
        print("⏳ Waiting for End Date field...")
        self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.END_DATE_FIELD)).click()
        print("✅ Clicked End Date box")
        self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.DATE_PICKER_DAY_CONTAINS(date_label))).click()
        print(f"✅ Selected End Date: {date_label}")

    def accept_terms(self):
        print("⏳ Waiting for Terms checkbox...")
        self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.TERMS_CHECKBOX)).click()
        print("✅ Accepted Terms and Conditions")

    def accept_rental_contracts(self):
        print("⏳ Waiting for Rental Contracts checkbox...")
        self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.CONTRACTS_CHECKBOX)).click()
        print("✅ Accepted Rental Contracts")

    def click_continue(self):
        print("⏳ Waiting for Continue button...")
        self.wait.until(EC.element_to_be_clickable(ServiceDetailsLocators.CONTINUE_AFTER_TERMS)).click()
        print("✅ Clicked Continue to next step")

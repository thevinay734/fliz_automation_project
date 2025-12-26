from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class EquipmentPage:
    def __init__(self, driver):
        self.driver = driver
        # 20 second का wait Jenkins के लिए बेहतर है
        self.wait = WebDriverWait(driver, 20)

    def select_equipment(self):
        try:
            # Cards का इंतज़ार करें
            elements = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH,
                     "//div[contains(@class, 'cursor-pointer') and contains(@class, 'hover:bg-backgroundHome')]")
                )
            )
            print(f"🟢 Found {len(elements)} equipment cards")

            if not elements:
                raise Exception("❌ No equipment cards found")

            # JS Click इस्तेमाल कर रहे हैं ताकि 'Element Intercepted' एरर न आए
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elements[0])
            self.driver.execute_script("arguments[0].click();", elements[0])
            print("✅ Clicked the first available equipment via JS")

        except TimeoutException:
            raise Exception("❌ Timeout: Equipment cards not found on page.")

    def click_continue(self):
        # normalize-space() से फालतू स्पेस की समस्या खत्म हो जाती है
        xpath = "//button[contains(normalize-space(), 'Continue')]"
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        # Jenkins/Headless के लिए Scroll और JS Click सबसे बेस्ट है
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        print("✅ Clicked 'Continue' button via JS")

    def wait_for_date_selection(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Start Date')]")))

    def increase_quantity(self, count):
        plus_button_xpath = "(//button[contains(@class,'quantity-btn')])[2]"
        plus_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, plus_button_xpath)))

        for i in range(count - 1):
            self.driver.execute_script("arguments[0].click();", plus_button)
            print(f"➕ Increased quantity: {i + 2}")

    def select_start_date(self, date_str):
        # Start Date फील्ड पर क्लिक
        start_date_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Start Date')]")))
        self.driver.execute_script("arguments[0].click();", start_date_input)

        # कैलेंडर से तारीख चुनना
        date_xpath = f"//div[@aria-label='{date_str}']"
        date_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        self.driver.execute_script("arguments[0].click();", date_element)
        print(f"📅 Selected Start Date: {date_str}")

    def select_end_date(self, date_str):
        # End Date फील्ड पर क्लिक
        end_date_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'End Date')]")))
        self.driver.execute_script("arguments[0].click();", end_date_input)

        # कैलेंडर से तारीख चुनना
        date_xpath = f"//div[@aria-label='{date_str}']"
        date_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        self.driver.execute_script("arguments[0].click();", date_element)
        print(f"📅 Selected End Date: {date_str}")

    def accept_terms(self):
        # Checkboxes के लिए JS click बहुत भरोसेमंद होता है
        terms = self.wait.until(EC.element_to_be_clickable((By.NAME, "termsCondition")))
        self.driver.execute_script("arguments[0].click();", terms)

        contracts = self.wait.until(EC.element_to_be_clickable((By.NAME, "rentalContracts")))
        self.driver.execute_script("arguments[0].click();", contracts)
        print("✅ Accepted Terms and Contracts")

    def click_continue_after_terms(self):
        # Span और Button दोनों को कवर करने वाला XPATH
        xpath = "//button[.//span[contains(text(), 'Continue')]] | //button[contains(text(), 'Continue')]"
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        print("✅ Clicked final 'Continue' after terms")
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EquipmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_equipment(self):
        try:
            elements = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH,
                     "//div[contains(@class, 'cursor-pointer') and contains(@class, 'hover:bg-backgroundHome')]")
                )
            )
            print(f"🟢 Found {len(elements)} equipment cards")

            if not elements:
                raise Exception("❌ No equipment cards found")

            elements[0].click()
            print("✅ Clicked the only available equipment")

        except TimeoutException:
            raise Exception("❌ Timeout: Equipment cards not found on page.")

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))).click()

    def wait_for_date_selection(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Start Date')]")))

    def increase_quantity(self, count):
        plus_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class,'quantity-btn')])[2]")))
        for _ in range(count - 1):
            plus_button.click()

    def select_start_date(self, date_str):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Start Date')]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{date_str}']"))).click()

    def select_end_date(self, date_str):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'End Date')]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{date_str}']"))).click()

    def accept_terms(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "termsCondition"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "rentalContracts"))).click()

    def click_continue_after_terms(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue')]"))).click()



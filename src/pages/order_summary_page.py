from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderSummaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_payment_method(self, index=0):
        radios = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']")))
        if radios:
            self.wait.until(EC.element_to_be_clickable(radios[index])).click()

    def click_pay_now(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'wpwl-button-pay')]"))).click()

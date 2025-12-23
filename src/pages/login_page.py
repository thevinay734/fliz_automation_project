from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    # Locators
    dropdown_country_xpath = "//div[contains(@class,'selected-flag')]"  # Click this to open dropdown
    search_country_input_class = "search-box"
    india_country_xpath = "//li[@data-country-code='in']"
    textbox_mobile_number_xpath = "//input[@placeholder='Member Phone Number']"
    textbox_password_id = "password"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def change_country(self):
        # Open country dropdown
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_country_xpath))).click()

    def select_country_india(self):
        # Search for 'ind' in country list
        search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.search_country_input_class)))
        search_input.clear()
        search_input.send_keys("ind")

        # Select India
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.india_country_xpath))).click()

    def set_mobile_number(self, mobile_number):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_mobile_number_xpath))).send_keys(mobile_number)

    def set_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id))).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))).click()

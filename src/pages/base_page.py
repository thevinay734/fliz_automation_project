from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time


class Dashboard:
    language_icon_css = "img[src='/images/browser.svg']"
    english_option_xpath = "//p[normalize-space()='English']"
    signin_button_xpath = "/html[1]/body[1]/div[1]/div[3]/div[3]/a[1]/span[1]"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page_to_load(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def click_language_icon(self):
        try:
            icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.language_icon_css)))
            self.driver.execute_script("arguments[0].click();", icon)
        except StaleElementReferenceException:
            time.sleep(1)  # short wait
            icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.language_icon_css)))
            self.driver.execute_script("arguments[0].click();", icon)

    def click_english_option(self):
        try:
            # Wait for the English option to appear and be clickable
            english = self.wait.until(EC.presence_of_element_located((By.XPATH, self.english_option_xpath)))
            self.driver.execute_script("arguments[0].click();", english)
        except Exception as e:
            raise Exception(f"❌ English option not clickable: {e}")

    def click_signin_button(self):
        try:
            signin_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.signin_button_xpath)))
            signin_button.click()
        except StaleElementReferenceException:
            time.sleep(1)
            signin_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.signin_button_xpath)))
            signin_button.click()
        except Exception as e:
            raise Exception(f"Signin button not clickable : {e}")

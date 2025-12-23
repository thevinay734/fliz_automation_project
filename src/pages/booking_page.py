from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def close_success_modal(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='cross icon']"))).click()

    def go_to_active_bookings(self):
        self.driver.get("https://dev.fliz.com.sa/en/booking/booking-active")

    def verify_booking_success(self):
        try:
            success_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Booking Confirmed')]"))
            )
            print(f"✅ Booking confirmed: {success_element.text}")
        except Exception as e:
            raise Exception("❌ Booking confirmation not found or took too long") from e

from selenium.webdriver.common.by import By


class DashboardLocators:
    CATEGORY_BY_TEXT = lambda name: (By.XPATH, f"//p[normalize-space()='{name}']")
    COMPANY_BY_NAME = lambda name: (By.XPATH, f"//p[contains(normalize-space(), '{name}')]")
    DUMP_TRUCKS = (By.XPATH, "//p[contains(text(), 'Dump Trucks')]")
    DUMP_6_TRUCKS = (By.XPATH, "//p[contains(text(), 'Dump 6 Trucks')]")
    DUMP_TRUCKS_SIDE_TIPPER = (By.XPATH, "//p[contains(text(), 'Dump Trucks Side Tipper')]")
    COMPANY_CARD = (By.XPATH, "//p[contains(text(), 'Great')]")


class EquipmentLocators:
    EQUIPMENT_CARDS = (By.XPATH, "//div[contains(@class, 'equipment-card')]")
    AVAILABLE_EQUIPMENT = (By.XPATH, "//div[contains(@class, 'mobile:justify-between')]")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")


class LoginLocators:
    PHONE_INPUT = (By.NAME, "phone")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log In')]")


class ServiceDetailsLocators:
    PLUS_BUTTON = (By.XPATH, "//img[@alt='plus']")
    START_DATE_FIELD = (By.XPATH, "//div[contains(text(), 'Start Date')]")
    END_DATE_FIELD = (By.XPATH, "//div[contains(text(), 'End Date')]")
    DATE_PICKER_DAY_BY_LABEL = lambda label: (By.XPATH, f"//div[@class='react-datepicker__day' and @aria-label='{label}']")
    DATE_PICKER_DAY_CONTAINS = lambda day: (
        By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}' and not(contains(@class, 'outside-month'))]"
    )
    TERMS_CHECKBOX = (By.ID, "termsCondition")
    CONTRACTS_CHECKBOX = (By.NAME, "rentalContracts")
    CONTINUE_AFTER_TERMS = (By.XPATH, "//span[contains(text(), 'Continue')]")


class OrderSummaryLocators:
    PAYMENT_OPTION = (By.XPATH, "//input[@type='radio']")
    PAY_NOW_BUTTON = (By.XPATH, "//button[contains(text(), 'Pay now')]")


class PaymentResultLocators:
    CLOSE_ICON = (By.XPATH, "//img[@alt='cross icon']")


class BookingPageLocators:
    ACTIVE_BOOKING_TAB = (By.XPATH, "//span[contains(text(), 'Home')]")

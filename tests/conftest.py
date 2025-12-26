import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService


# 1. यह फंक्शन Pytest को बताता है कि '--browser_name' एक मान्य कमांड है
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox"
    )


@pytest.fixture(scope="function")
def setup(request):
    # 2. यहाँ हम कमांड लाइन से पास की गई वैल्यू को पढ़ते हैं
    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        # Jenkins (Linux/Mac Server) के लिए अक्सर headless मोड की ज़रूरत होती है
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    driver.maximize_window()
    yield driver
    driver.quit()
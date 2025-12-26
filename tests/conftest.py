import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        chrome_options = Options()
        # --- ये 3 लाइनें Headless के लिए ज़रूरी हैं ---
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # ------------------------------------------

        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        # Firefox के लिए भी headless कर सकते हैं
        from selenium.webdriver.firefox.options import Options as FFOptions
        ff_options = FFOptions()
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(options=ff_options)

    driver.maximize_window()
    yield driver
    driver.quit()
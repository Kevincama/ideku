import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.config import BrowserConfig
from utility import ChromeOptions, EdgeOptions


@pytest.fixture
def browser_driver(request):
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == BrowserConfig.CHROME.value:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=ChromeOptions().get_options()
        )
    elif browser_name == BrowserConfig.EDGE.value:
        driver = webdriver.Edge(
            service=Service(EdgeChromiumDriverManager().install()),
            options=EdgeOptions().get_options()
        )

    yield driver
    driver.quit()

import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import DEFAULT_TIMEOUT
from utility import logger_func


# Add _ means that those function should not use in test.py file.
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @logger_func
    def _wait_element_display(self, locator_info: str, timeout=DEFAULT_TIMEOUT):
        try:
            return (
                WebDriverWait(driver=self.driver, timeout=timeout).
                until(
                    EC.presence_of_element_located(
                        locator=(locator_info[0], locator_info[1])
                    )
                )
            )
        except Exception as e:
            pytest.fail(f"Element not display: {e}")

    @logger_func
    def _find_element_info(self, locator_info: str, timeout=DEFAULT_TIMEOUT):
        try:
            return (
                WebDriverWait(driver=self.driver, timeout=timeout).
                until(
                    EC.visibility_of_element_located(
                        locator=(locator_info[0], locator_info[1])
                    )
                )
            )
        except Exception as e:
            pytest.fail(f"Element not existed: {e}")

    @logger_func
    def _find_elements_info(self, locator_info: str, timeout=DEFAULT_TIMEOUT):
        try:
            return (
                WebDriverWait(driver=self.driver, timeout=timeout).
                until(
                    EC.visibility_of_element_located
                    (locator=(locator_info[0], locator_info[1])
                     )
                )
            )
        except Exception as e:
            pytest.fail(f"Elements not existed: {e}")

    @logger_func
    def _click_element(self, element: WebElement):
        try:
            element.click()
        except Exception as e:
            pytest.fail(f"Click element fail, element: {element}, Exception: {e}")

    @logger_func
    def _check_element_display(self, element: WebElement):
        try:
            return element.is_displayed()
        except Exception as e:
            pytest.fail(f"Element is not display, element: {element}, Exception: {e}")

    @logger_func
    def _check_webpage_load_complete(self):
        try:
            if not self.driver.execute_script('return document.readyState') == 'complete':
                pytest.fail(f"WebPage not load complete")
        except Exception as e:
            pytest.fail(f"WebPage not load complete, maybe over timeout, Exception: {e}")

    @logger_func
    def _input_to_element(self, element, input_str):
        try:
            element.send_keys(input_str)
        except Exception as e:
            pytest.fail(f"Input text to field error, Exception: {e}")

    @logger_func
    def _switch_browser_to_newtab(self):
        try:
            current_tab = self.driver.current_window_handle
            all_tabs = self.driver.window_handles

            for tab in all_tabs:
                if tab != current_tab:
                    self.driver.switch_to.window(tab)
                    break

        except Exception as e:
            pytest.fail(f"Switch to new tab error, Exception: {e}")

    @logger_func
    def _check_btn_enable_status(self, ele):
        try:
            return ele.is_enabled()
        except Exception as e:
            pytest.fail(f"Check element {ele} btn status fail, Exception: {e}")


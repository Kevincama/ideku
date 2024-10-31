from pages.base_page import BasePage
from .locators import MainPageElements
from utility import logger_func


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageElements

    @logger_func
    def check_logo_display(self):
        self._wait_element_display(self.locators.mainpage_logo)
        ele = self._find_element_info(self.locators.mainpage_logo, timeout=10)
        return self._check_element_display(ele)

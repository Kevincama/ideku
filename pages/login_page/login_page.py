from pages.base_page import BasePage
from .locators import LoginPageElements
from utility import logger_func


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageElements

    @logger_func
    def check_logo_display(self):
        ele = self._find_element_info(self.locators.logo_img, timeout=10)
        return self._check_element_display(ele)

    @logger_func
    def input_account(self, account: str):
        ele = self._find_element_info(self.locators.username_input_field)
        self._input_to_element(ele, account)

    @logger_func
    def input_pwd(self, pwd: str):
        ele = self._find_element_info(self.locators.pwd_input_field)
        self._input_to_element(ele, pwd)

    @logger_func
    def check_warning_hint_display(self):
        ele = self._find_element_info(self.locators.warning_hint)
        return self._check_element_display(ele)

    @logger_func
    def click_login_btn(self):
        ele = self._find_element_info(self.locators.login_btn)
        self._click_element(ele)

    @logger_func
    def check_page_load_complete(self):
        self._check_webpage_load_complete()

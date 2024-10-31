import time
from time import sleep

import pytest

from pages import LoginPage, MainPage
from testdata import load_test_data


class TestRegisterFlow:

    @pytest.fixture(autouse=True)
    def setup(self, browser_driver):
        self.browser_driver = browser_driver
        self.login_page = LoginPage(self.browser_driver)

    @pytest.mark.p0
    @pytest.mark.parametrize('load_test_data', ['login_flow.json'], indirect=True)
    def test_login_success(self, load_test_data):
        testdata = load_test_data['LOGIN_SUCCESS']
        test_url = testdata['TEST_URL']
        test_account = testdata['TEST_DATA']['ACCOUNT']
        test_pwd = testdata['TEST_DATA']['PWD']

        expect_result = testdata['EXPECT_RESULT']['LOGO_DISPLAY']

        self.browser_driver.get(test_url)
        assert self.login_page.check_logo_display() == True, "The login page not display correct, logo not exist"
        self.login_page.input_account(test_account)
        self.login_page.input_pwd(test_pwd)
        self.login_page.click_login_btn()

        main_page = MainPage(self.browser_driver)
        assert main_page.check_logo_display() == expect_result

    @pytest.mark.rt
    @pytest.mark.parametrize('load_test_data', ['login_flow.json'], indirect=True)
    def test_login_fail_with_wrong_account(self, load_test_data):
        testdata = load_test_data['LOGIN_FAIL_WRONG_ACCOUNT']
        test_url = testdata['TEST_URL']
        test_account = testdata['TEST_DATA']['ACCOUNT']
        test_pwd = testdata['TEST_DATA']['PWD']

        expect_result = testdata['EXPECT_RESULT']['WARNING_HINT_DISPLAY']

        self.browser_driver.get(test_url)
        assert self.login_page.check_logo_display() == True, "The login page not display correct, logo not exist"
        self.login_page.input_account(test_account)
        self.login_page.input_pwd(test_pwd)
        self.login_page.click_login_btn()

        assert self.login_page.check_warning_hint_display() == expect_result

    @pytest.mark.rt
    @pytest.mark.parametrize('load_test_data', ['login_flow.json'], indirect=True)
    def test_login_fail_with_wrong_pwd(self, load_test_data):
        testdata = load_test_data['LOGIN_FAIL_WRONG_ACCOUNT']
        test_url = testdata['TEST_URL']
        test_account = testdata['TEST_DATA']['ACCOUNT']
        test_pwd = testdata['TEST_DATA']['PWD']

        expect_result = testdata['EXPECT_RESULT']['WARNING_HINT_DISPLAY']

        self.browser_driver.get(test_url)
        assert self.login_page.check_logo_display() == True, "The login page not display correct, logo not exist"
        self.login_page.input_account(test_account)
        self.login_page.input_pwd(test_pwd)
        self.login_page.click_login_btn()

        assert self.login_page.check_warning_hint_display() == expect_result

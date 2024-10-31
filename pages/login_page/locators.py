from selenium.webdriver.common.by import By


class LoginPageElements:
    username_input_field = (By.CSS_SELECTOR, 'input[name="username"]')
    pwd_input_field = (By.CSS_SELECTOR, 'input[name="password"]')
    warning_hint = (By.CSS_SELECTOR, 'p.oxd-text.oxd-alert-content-text')
    login_btn = (By.CSS_SELECTOR, 'button.oxd-button.oxd-button--main')
    logo_img = (By.CSS_SELECTOR, 'img[alt="company-branding"]')

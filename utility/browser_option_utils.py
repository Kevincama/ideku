from selenium import webdriver


class BaseOptions:
    def __init__(self):
        self.options = self.create_options()

    def create_options(self):
        raise NotImplementedError("Should use this function directly")

    def get_options(self):
        return self.options


class ChromeOptions(BaseOptions):
    def create_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        #options.add_argument("--headless") # If using docker that can unmark this
        options.add_argument("--inprivate")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        return options


class EdgeOptions(BaseOptions):
    def create_options(self):
        options = webdriver.EdgeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        #options.add_argument("--headless") # If using docker that can unmark this
        options.add_argument("--inprivate")
        return options

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what) -> WebElement | bool:
        """Check present element"""
        try:
            obj = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return obj

    def get_element(self, locator: tuple) -> WebElement:
        """Get element. Locator - class attribute from locators.py file"""
        return self.is_element_present(*locator)

    def open(self):
        self.browser.get(self.url)



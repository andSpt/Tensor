from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser: WebDriver, url: str, timeout: int = 15) -> None:
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def is_element_present(self, locator: tuple[str, str]) -> WebElement | bool:
        """Searches for a web element on an HTML page"""
        try:
            obj = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            return False
        return obj

    def is_element_clickable(self, locator: tuple[str, str]) -> WebElement | bool:
        """Searches for a web element on an HTML page until it is clickable."""
        try:
            obj = WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False
        return obj

    def is_element_visibility(self, locator: tuple[str, str]) -> WebElement | bool:
        """Searches for a web element on an HTML page until it is visible."""
        try:
            obj = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
        except NoSuchElementException:
            return False
        return obj

    def is_element_to_be_present_text(self, locator: tuple[str, str], text: str) -> bool:
        """Searches for a web element on an HTML page until it contains text like in the template."""
        try:
            result: bool = WebDriverWait(self.browser, self.timeout).until(EC.text_to_be_present_in_element(locator=locator, text_=text))
        except NoSuchElementException:
            return False
        return result

    def open(self) -> None:
        self.browser.get(self.url)



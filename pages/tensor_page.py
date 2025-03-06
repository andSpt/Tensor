from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators import TensorLocators


class TensorPage(BasePage):

    def should_be_strength_in_people(self) -> WebElement:
        """Find and return WebElement 'strength_in_people' or Assertion error"""
        assert (strength_in_people := self.is_element_present(
            TensorLocators.BLOCK_STRENGTH_IN_PEOPLE)), "отсутствует блок 'Сила в людях'"
        return strength_in_people

    def should_be_strength_in_people_more_details(self) -> WebElement:
        """Find and return WebElement 'strength in people more_details' or Assertion error"""
        assert (more_details := self.is_element_present(TensorLocators.MORE_DETAILS)), "отсутствует блок 'Сила в людях'"
        return more_details





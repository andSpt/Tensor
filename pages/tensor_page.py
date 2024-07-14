from typing import NoReturn

import time
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from pages.tensor_more_details import TensorMoreDetails
from locators import TensorLocators, TensorMoreDetailsLocators


class TensorPage(BasePage):

    def __init__(self, browser, url, timeout=10) -> None:
        super().__init__(browser, url, timeout)

    def should_be_tensor_url(self) -> NoReturn:
        """Check the URL contains a tensor.ru. Noreturn or Assertion error"""
        current_url: str = self.browser.current_url
        assert "tensor" in current_url, "There is no 'tensor' in the link"

    def should_be_strength_in_people(self) -> WebElement:
        """Find and return WebElement 'strength_in_people' or Assertion error"""
        assert (strength_in_people_text := self.get_element(
            TensorLocators.STRENGHT_IS_IN_PEOPLE_TEXT)), "strength_in_people_text is not presented"
        return strength_in_people_text

    def should_be_strength_in_people_more_details_link(self) -> WebElement:
        """Find and return WebElement 'strength in people more_details' or Assertion error"""
        assert (strength_in_people_more_details_link := self.get_element(
            TensorLocators.STRENGHT_IS_IN_PEOPLE_MORE_DETAILS)), "should_be_strength_in_people_more_details_link is not presented"
        return strength_in_people_more_details_link

    def go_to_tensor_more_details(self) -> TensorMoreDetails:
        """Run function should_be_strength_in_people_more_details_link
        Open page 'more details' and return objects TensorMoreDetails"""
        tensor_more_details: WebElement = self.should_be_strength_in_people_more_details_link()
        self.browser.execute_script("arguments[0].scrollIntoView(true);", tensor_more_details)
        # time.sleep(0.44)
        tensor_more_details_page: TensorMoreDetails = TensorMoreDetails(self.browser, tensor_more_details.get_attribute('href'))
        tensor_more_details_page.open()
        return tensor_more_details_page




from typing import NoReturn
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.tensor_page import TensorPage
from locators import SbisContactsLocators


class SbisContactsPage(BasePage):

    def should_be_tensor_banner(self) -> WebElement:
        """Check and return WebElement tensor banner,
        Assertion error if not this element"""
        assert (banner_tensor := self.is_element_present(SbisContactsLocators.BANNER_TENSOR)), "нет баннера Тензор"
        return banner_tensor

    def should_be_region(self) -> WebElement:
        """Check and return WebElement region or Assertion error"""
        assert (region := self.is_element_present(SbisContactsLocators.REGION)), "не определяется местоположение"
        return region

    def should_be_list_partners(self) -> WebElement:
        """Check and return WebElement list_partners or Assertion error"""
        assert (
            list_partners := self.is_element_present(SbisContactsLocators.LIST_PARTNERS)), "отсутствует список партнеров"
        return list_partners

    def should_be_new_region(self) -> WebElement:
        """Check and return WebElement new_region or Assertion error"""
        assert (new_region := self.is_element_clickable(SbisContactsLocators.REGION_KAMCHATKA)), "новый регион отсутствует в списке"
        return new_region

    def should_be_present_text_new_region(self) -> None:
        """Check text into WebElement new_region or Assertion error"""
        assert self.is_element_to_be_present_text(
            locator=SbisContactsLocators.REGION, text="Камчатский край"
        ), "Выбран не Камчатский Край или не найден регион"

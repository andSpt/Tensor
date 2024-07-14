from pages.base_page import BasePage
from locators import SBISLocators, SBISContactsLocators
from selenium.webdriver.remote.webelement import WebElement


class SbisPage(BasePage):

    def __init__(self, browser, url, timeout=10) -> None:
        super().__init__(browser, url, timeout)


    def should_be_contacts(self) -> WebElement:
        """Check element contacts is present"""
        assert (sbis_contasts_header := self.get_element(
            SBISLocators.SBIS_CONTASTS)), "sbis_contasts_header' is not presented"
        return sbis_contasts_header

    def should_be_tensor_banner(self) -> WebElement:
        """Check element banner tensor is present"""
        assert (banner_tensor := self.get_element(SBISContactsLocators.BANNER_TENSOR)), "banner_tensor is not presented"
        return banner_tensor





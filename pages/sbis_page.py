from pages.base_page import BasePage
from locators import SBISLocators, SBISContactsLocators, TensorLocators, TensorMoreDetailsLocators


class SbisPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_be_contacts(self):
        assert (sbis_contasts_header := self.get_element(
            SBISLocators.SBIS_CONTASTS)), "sbis_contasts_header' is not presented"
        return sbis_contasts_header


    def should_be_tensor_banner(self):
        assert (banner_tensor := self.get_element(SBISContactsLocators.BANNER_TENSOR)), "banner_tensor is not presented"
        return banner_tensor





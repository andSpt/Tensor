from pages.base_page import BasePage
from locators import SBISContactsLocators


class SbisContacts(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.your_region = 'Нижегородская обл.'

    def should_be_tensor_banner(self):
        assert (banner_tensor := self.get_element(SBISContactsLocators.BANNER_TENSOR)), "banner_tensor is not presented"
        return banner_tensor

    def should_be_your_region(self):
        pass

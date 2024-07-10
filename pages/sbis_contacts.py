from pages.base_page import BasePage
from locators import SBISContactsLocators


class SbisContacts(BasePage):

    def should_be_tensor_banner(self):
        assert (banner_tensor := self.get_element(SBISContactsLocators.BANNER_TENSOR)), "banner_tensor is not presented"
        return banner_tensor


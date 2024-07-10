from pages.base_page import BasePage
from locators import SBISLocators


class SbisPage(BasePage):

    def should_be_contacts(self):
        assert (sbis_contasts_header := self.get_element(
            SBISLocators.SBIS_CONTASTS)), "sbis_contasts_header' is not presented"
        return sbis_contasts_header





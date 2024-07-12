from pages.base_page import BasePage
from locators import TensorLocators, TensorMoreDetailsLocators


class TensorPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_be_tensor_url(self):
        """Проверка на url-адрес"""
        current_url = self.browser.current_url
        assert "tensor" in current_url, "There is no 'tensor' in the link"

    def should_be_strength_in_people(self):
        assert (strength_in_people_text := self.get_element(
            TensorLocators.STRENGHT_IS_IN_PEOPLE_TEXT)), "strength_in_people_text is not presented"
        return strength_in_people_text


    def should_be_strength_in_people_more_details_link(self):
        assert (strength_in_people_more_details_link := self.get_element(
            TensorLocators.STRENGHT_IS_IN_PEOPLE_MORE_DETAILS)), "should_be_strength_in_people_more_details_link is not presented"
        return strength_in_people_more_details_link






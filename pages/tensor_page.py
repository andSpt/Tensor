from pages.base_page import BasePage
from locators import TensorLocators


class TensorPage(BasePage):

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



    def should_be_image_image_accompanying_clients(self):
        assert (image_accompanying_clients := self.get_element(
            TensorLocators.IMAGE_ACCOMPANYING_CLIENT)), "image_accompanying_clients is not presented"
        return image_accompanying_clients


    def should_be_contacts(self):
        assert (link := self.get_element(TensorLocators.SBIS_CONTASTS)), "sbis_contacts is not presented"
        link.click()
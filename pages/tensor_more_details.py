from pages.base_page import BasePage
from locators import TensorMoreDetailsLocators


class TensorMoreDetails(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def should_be_image_develop_sbis(self):
        assert (image_develop_sbis := self.get_element(
            TensorMoreDetailsLocators.IMAGE_DEVELOP_SBIS)), "image_develop_sbis is not presented"
        return image_develop_sbis


    def should_be_image_promote_services(self):
        assert (image_promote_services := self.get_element(
            TensorMoreDetailsLocators.IMAGE_PROMOTE_SERVICES)), "image_promote_services is not presented"
        return image_promote_services


    def should_be_image_create_infrastructure(self):
        assert (image_create_infrastructure := self.get_element(
            TensorMoreDetailsLocators.IMAGE_CREATE_INFRASTRUCTURE)), "image_create_infrastructure is not presented"
        return image_create_infrastructure


    def should_be_image_image_accompanying_clients(self):
        assert (image_accompanying_clients := self.get_element(
            TensorMoreDetailsLocators.IMAGE_ACCOMPANYING_CLIENT)), "image_accompanying_clients is not presented"
        return image_accompanying_clients


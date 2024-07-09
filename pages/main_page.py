from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class PageObject(BasePage):

    def should_be_contacts(self):
        assert (sbis_contasts_header := self.get_element(
            ProductPageLocators.SBIS_CONTASTS)), "sbis_contasts_header' is not presented"
        return sbis_contasts_header

    def should_be_tenzor_banner(self):
        assert (banner_tenzor := self.get_element(ProductPageLocators.BANNER_TENZOR)), "banner_tenzor is not presented"
        return banner_tenzor

    def should_be_strength_in_people(self):
        assert (strength_in_people_text := self.get_element(ProductPageLocators.STRENGHT_IS_IN_PEOPLE_TEXT)), "strength_in_people_text is not presented"
        return strength_in_people_text

    def should_be_strength_in_people_more_details_link(self):
        assert (strength_in_people_more_details_link := self.get_element(
            ProductPageLocators.STRENGHT_IS_IN_PEOPLE_MORE_DETAILS)), "should_be_strength_in_people_more_details_link is not presented"
        return strength_in_people_more_details_link

    def should_be_image_develop_sbis(self):
        assert (image_develop_sbis := self.get_element(
            ProductPageLocators.IMAGE_DEVELOP_SBIS)), "image_develop_sbis is not presented"
        return image_develop_sbis

    def should_be_image_promote_services(self):
        assert (image_promote_services := self.get_element(
            ProductPageLocators.IMAGE_PROMOTE_SERVICES)), "image_promote_services is not presented"
        return image_promote_services

    def should_be_image_create_infrastructure(self):
        assert (image_create_infrastructure := self.get_element(
            ProductPageLocators.IMAGE_CREATE_INFRASTRUCTURE)), "image_create_infrastructure is not presented"
        return image_create_infrastructure

    def should_be_image_image_accompanying_clients(self):
        assert (image_accompanying_clients := self.get_element(
            ProductPageLocators.IMAGE_CREATE_INFRASTRUCTURE)), "image_accompanying_clients is not presented"
        return image_accompanying_clients


    def go_to_basket_page(self):
        assert (link := self.get_element(ProductPageLocators.BASKET_LINK)), "Link to busket is not presented"
        link.click()
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators import AboutLocators


class AboutPage(BasePage):

    def should_be_img_dev_sistem_saby(self) -> WebElement:
        assert (img := self.is_element_present(AboutLocators.IMG_DEV_SISTEM_SABY)), "отсутствует картинка 'Разрабатываем систему'"
        return img

    def should_be_img_promote_services(self) -> WebElement:
        assert (img := self.is_element_present(AboutLocators.IMG_PROMOTE_SERVICES)), "отсутствует картинка 'Продвигаем сервисы'"
        return img

    def should_be_img_create_infrastructure(self) -> WebElement:
        assert (img := self.is_element_present(AboutLocators.IMG_CREATE_INFRASTRUCTURE)), "отсутствует картинка 'Создаем инфраструктуру'"
        return img

    def should_be_img_assist_cliens(self) -> WebElement:
        assert (img := self.is_element_present(AboutLocators.IMG_ASSIST_CLIENTS)), "отсутствует картинка 'Сопровождаем клиентов'"
        return img

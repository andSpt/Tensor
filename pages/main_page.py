from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    def should_be_contacts(self) -> WebElement:
        """Find and return WebElement 'contacts' or Assertion error"""
        assert (contacts := self.is_element_present(MainPageLocators.CONTACTS)), "нет кнопки 'Контакты'"
        return contacts

    def should_be_contacts_more(self) -> WebElement:
        """Find and return WebElement 'contacts_more' is present or Assertion error"""
        assert (contacts_more := self.is_element_present(
            MainPageLocators.CONTACTS_MORE)), "нет кнопки 'Еще 25 офисов в регионе'"
        return contacts_more

    def should_be_download_local_versions(self) -> WebElement:
        """Find and return WebElement 'download_local_versions' is present or Assertion error"""
        assert (download_local_versions := self.is_element_present(
            MainPageLocators.DOWNLOAD_LOCAL_VERSIONS)), "нет кнопки 'Скачать локальные версии'"
        return download_local_versions






from typing import NoReturn

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.tensor_page import TensorPage
from locators import SBISContactsLocators
import time


class SbisContacts(BasePage):

    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        super().__init__(browser, url, timeout)
        self.my_region_ru: str = 'г. Москва'
        self.my_region_en: str = 'moskva'
        self.test_region_ru: str = 'Камчатский край'
        self.test_region_en: str = 'kamchatskij-kraj'

    def should_be_tensor_banner(self) -> WebElement:
        """Return WebDriver element banner tensor or  or Assertion Error"""
        assert (banner_tensor := self.get_element(SBISContactsLocators.BANNER_TENSOR)), "banner_tensor is not presented"
        return banner_tensor

    def go_to_tensor(self) -> TensorPage:
        """Click tensor banner and go to tensor.ru"""
        tensor_banner: WebElement = self.should_be_tensor_banner()
        # time.sleep(0.44)
        tensor_page: TensorPage = TensorPage(self.browser, tensor_banner.get_attribute('href'))
        tensor_page.open()
        return tensor_page


    def should_be_region(self) -> WebElement:
        """Return WebElement my_region or Assertion Error"""
        assert (region := WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(SBISContactsLocators.MY_REGION))
                ), "Region is not presented"
        # assert (banner_tensor := self.get_element(SBISContactsLocators.BANNER_TENSOR)), "banner_tensor is not presented"
        return region

        # assert (region := self.get_element(SBISContactsLocators.MY_REGION)), "Region is not presented"
        # return region

    def should_be_list_partners(self) -> list[str | None]:
        """Return list of partners in the selected region or Assertion error if not this element"""
        assert (containers := self.browser.find_elements("class name", "sbisru-Contacts-List__name")), "List_partners is not presented"
        list_partners = []
        if containers:
            for container in containers:
                partner_name = container.get_attribute("title")
                list_partners.append(partner_name)
        assert list_partners != [], "List_partners is empty"
        return list_partners

    def should_be_my_region_into_url(self) -> NoReturn:
        """checking if the URL matches my region"""
        current_url = self.browser.current_url
        assert self.my_region_en in current_url, "There is no my_region in the URL"

    def change_region_to_kamchat_krai(self) -> WebElement:
        """"checking that my region is Kamchatka krai"""
        assert (new_region := WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(SBISContactsLocators.REGION_KAMCHAT_KRAI))
                ), "Region Kamchatskiy krai is not presented"
        # assert (new_region := self.get_element(SBISContactsLocators.REGION_KAMCHAT_KRAI)), "Region Kamchatskiy krai is not presented"
        return new_region





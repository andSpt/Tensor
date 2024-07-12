from pages.base_page import BasePage
from locators import SBISContactsLocators


class SbisContacts(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.my_region_ru = 'г. Москва'
        self.my_region_en = 'moskva'
        self.test_region_ru = 'Камчатский край'
        self.test_region_en = 'kamchatskij-kraj'

    def should_be_tensor_banner(self):
        assert (banner_tensor := self.get_element(SBISContactsLocators.BANNER_TENSOR)), "banner_tensor is not presented"
        return banner_tensor

    def should_be_region(self):
        assert (region := self.get_element(SBISContactsLocators.MY_REGION)), "Region is not presented"
        return region

    def should_be_list_partners(self):
        assert (containers := self.browser.find_elements("class name", "sbisru-Contacts-List__name")), "List_partners is not presented"
        list_partners = []
        if containers:
            for container in containers:
                partner_name = container.get_attribute("title")
                list_partners.append(partner_name)
        assert list_partners != [], "List_partners is empty"
        return list_partners

    def should_be_my_region_into_url(self):
        current_url = self.browser.current_url
        assert self.my_region_en in current_url, "There is no my_region in the URL"

    def change_region_to_kamchat_krai(self):
        assert (new_region := self.get_element(SBISContactsLocators.REGION_KAMCHAT_KRAI)), "Region Kamchatskiy krai is not presented"
        return new_region





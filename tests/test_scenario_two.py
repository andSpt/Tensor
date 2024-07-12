import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.sbis_contacts import SbisContacts
from pages.tensor_more_details import TensorMoreDetails
import time

def test_scenario_two(browser):
    link = "https://sbis.ru/"
    sbis_page: SbisPage = SbisPage(browser, link)
    sbis_page.open()

    # Проверяем СБИС контакты
    contacts = sbis_page.should_be_contacts()

    #Переходим в СБИС контакты
    contacts.click()
    # time.sleep(1)
    sbis_contacts: SbisContacts = SbisContacts(browser, browser.current_url)

    #Проверяем совпадение региона
    region = sbis_contacts.should_be_region()
    assert region.text == sbis_contacts.my_region_ru, "Region is not match"
    print("region ok")

    #Проверяем список партнеров
    list_partners = sbis_contacts.should_be_list_partners()
    print("list_partners ok", list_partners)

    #Проверяем регион в URL
    sbis_contacts.should_be_my_region_into_url()

    #Открываем список регионов
    region.click()
    time.sleep(1)
    #Меняем выбираем Камчатский край
    kamchat_region = sbis_contacts.change_region_to_kamchat_krai()
    print(kamchat_region.text)
    time.sleep(1)
    kamchat_region.click()
    time.sleep(1)
    #Проверяем выбранный регион - Камчатский край
    current_region = sbis_contacts.should_be_region()
    assert current_region.text == sbis_contacts.test_region_ru

    #Проверяем регион в URL - Камчатский край
    current_url = sbis_contacts.browser.current_url
    assert sbis_contacts.test_region_en in current_url, "There is no 'kamchatskij-kraj' in the URL"

    # Проверяем список партнеров в Камчатском регионе
    list_partners_in_kamchat_krai = sbis_contacts.should_be_list_partners()
    assert list_partners != list_partners_in_kamchat_krai, f"List partners in Kamchatskij krai match to {sbis_contacts.my_region_en}"

















import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.main_page import MainPage
from pages.sbis_contacts_page import SbisContactsPage


load_dotenv()

def test_two(browser: webdriver) -> None:
    link: str = 'https://sbis.ru/'
    main_page: MainPage = MainPage(browser, link, 10)
    main_page.open()

    contacts: WebElement = main_page.should_be_contacts()
    contacts.click()
    contacts_more: WebElement = main_page.should_be_contacts_more()
    contacts_more.click()

    sbis_contacts_page: SbisContactsPage = SbisContactsPage(browser, browser.current_url)
    current_region: WebElement = sbis_contacts_page.should_be_region()

    selected_region = os.getenv("REGION")
    selected_city = os.getenv("CITY")
    assert current_region.text == selected_region, "Неправильно определилось местоположение"

    list_partners: WebElement = sbis_contacts_page.should_be_list_partners()
    assert list_partners.text == selected_city, "Не правильный список партнеров"

    current_region.click()
    new_region: WebElement = sbis_contacts_page.should_be_new_region()
    new_region.click()

    sbis_contacts_page.should_be_present_text_new_region()
    new_list_partners: WebElement = sbis_contacts_page.should_be_list_partners()
    assert new_list_partners.text == "Петропавловск-Камчатский", "Список партнеров не Камчатка"

    current_url: str = browser.current_url
    assert "41-kamchatskij-kraj" in current_url, "В адресе нет Камчатского края"

    page_title: str = browser.title
    assert "Камчатский край" in page_title, "В тексте заголовка нет Камчатского края"

















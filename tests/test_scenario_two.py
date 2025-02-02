import time

from selenium.webdriver.remote.webelement import WebElement

from pages.sbis_page import SbisPage
from pages.sbis_contacts import SbisContacts


def test_scenario_two(browser) -> None:
    link: str = "https://sbis.ru/"
    sbis_page: SbisPage = SbisPage(browser, link)
    sbis_page.open()

    # Проверяем СБИС контакты
    contacts: WebElement = sbis_page.should_be_contacts()

    # Переходим в СБИС контакты
    contacts.click()

    time.sleep(0.44)

    sbis_contacts: SbisContacts = SbisContacts(browser, browser.current_url)

    # Проверяем совпадение региона
    region: WebElement = sbis_contacts.should_be_region()
    assert region.text == sbis_contacts.my_region_ru, "Region is not match"

    # Проверяем список партнеров
    list_partners: list[str] = sbis_contacts.should_be_list_partners()

    # Проверяем регион в URL
    sbis_contacts.should_be_my_region_into_url()

    # Открываем список регионов
    region.click()
    time.sleep(0.44)

    # Выбираем Камчатский край
    kamchat_region: WebElement = sbis_contacts.should_be_region_to_kamchat_krai()

    time.sleep(0.44)

    kamchat_region.click()

    time.sleep(0.55)

    # Проверяем выбранный регион - Камчатский край
    current_region: WebElement = sbis_contacts.should_be_region()
    assert current_region.text == sbis_contacts.test_region_ru

    # Проверяем регион в URL - Камчатский край
    current_url: str = sbis_contacts.browser.current_url
    assert sbis_contacts.test_region_en in current_url, "There is no 'kamchatskij-kraj' in the URL"

    # Проверяем список партнеров в Камчатском регионе
    list_partners_in_kamchat_krai = sbis_contacts.should_be_list_partners()
    assert list_partners != list_partners_in_kamchat_krai, f"List partners in Kamchatskij krai match to {sbis_contacts.my_region_en}"

















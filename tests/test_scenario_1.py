from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.main_page import MainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage


def test_one(browser: webdriver) -> None:
    link: str = 'https://sbis.ru/'

    main_page: MainPage = MainPage(browser, link, 10)
    main_page.open()

    contacts: WebElement = main_page.should_be_contacts()
    contacts.click()

    contacts_more: WebElement = main_page.should_be_contacts_more()
    contacts_more.click()

    sbis_contacts_page: SbisContactsPage = SbisContactsPage(browser, browser.current_url)

    tensor_banner: WebElement = sbis_contacts_page.should_be_tensor_banner()
    tensor_banner.click()

    sbis_contacts_window: str = browser.window_handles[0]
    tensor_window: str = browser.window_handles[1]
    browser.switch_to.window(tensor_window)

    tensor_page: TensorPage = TensorPage(browser, browser.current_url)

    strength_in_people: WebElement = tensor_page.should_be_strength_in_people()
    browser.execute_script("arguments[0].scrollIntoView();", strength_in_people)

    more_details: WebElement = tensor_page.should_be_strength_in_people_more_details()
    more_details.click()

    about_page: AboutPage = AboutPage(browser, browser.current_url)

    img_dev_sistem_saby: WebElement = about_page.should_be_img_dev_sistem_saby()

    browser.execute_script("arguments[0].scrollIntoView();", img_dev_sistem_saby)

    img_promote_services: WebElement = about_page.should_be_img_promote_services()
    img_assist_cliens: WebElement = about_page.should_be_img_assist_cliens()
    img_create_infrastructure: WebElement = about_page.should_be_img_create_infrastructure()

    images: List[WebElement] = [img_dev_sistem_saby,  img_promote_services, img_assist_cliens, img_create_infrastructure]

    height: int = img_dev_sistem_saby.size["height"]
    width: int = img_dev_sistem_saby.size["width"]

    for img in images[1:]:
        assert img.size["height"] == height, 'Высота картинок не совпадает'
        assert img.size["width"] == width, 'Ширина картинок не совпадает'

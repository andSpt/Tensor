import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.sbis_contacts import SbisContacts
from pages.tensor_more_details import TensorMoreDetails


def test_scenario_one(browser):
    link = "https://sbis.ru/"
    sbis_page: SbisPage = SbisPage(browser, link)
    sbis_page.open()

    #Проверяем СБИС контакты
    contacts = sbis_page.should_be_contacts()

    #Переходим в СБИС контакты
    contacts.click()

    sbis_contacts: SbisContacts = SbisContacts(browser, browser.current_url)

    #Проверяем баннер Тензор
    tensor_banner = sbis_contacts.should_be_tensor_banner()

    #Проходим на tensor.ru
    tensor_banner.click()

    tensor_page: TensorPage = TensorPage(browser, browser.current_url)

    #Проверяем, что мы на сайте tensor.ru
    tensor_page.should_be_tensor_url()

    # Проверяем блок "Сила в людях"
    tensor_page.should_be_strength_in_people()

    # Проверяем блок "Сила в людях"
    tensor_page.should_be_strength_in_people()

    # Проверяем блок "Сила в людях"
    tensor_page.should_be_strength_in_people()

    # Проверяем блок "Подробнее"
    tensor_more_details = tensor_page.should_be_strength_in_people_more_details_link()

    #Проходим на tensor more_details
    tensor_more_details.click()

    tensor_more_details_page: TensorMoreDetails = TensorMoreDetails(browser, browser.current_url)

    tensor_more_details_page.should_be_image_develop_sbis()

    tensor_more_details_page.should_be_image_promote_services()

    tensor_more_details_page.should_be_image_create_infrastructure()

    tensor_more_details_page.should_be_image_image_accompanying_clients()








    #Проверяем, что мы на сайте tensor.tu
    # current_url = page.browser.current_url
    # assert "tensor.ru" in current_url, f"Expected URL 'tensor.ru', but got {current_url}"
    #
    # tensor_page: Tensor_page = Tensor_page(browser, link)
    # tensor_page.open()

    # #Проверяем, что есть блок "Сила в людях"
    # tensor_page.






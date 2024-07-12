import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.sbis_contacts import SbisContacts
from pages.tensor_more_details import TensorMoreDetails
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException



def test_scenario_one(browser):
    link = "https://sbis.ru/"
    page: SbisPage = SbisPage(browser, link)
    page.open()

    #Проверяем СБИС контакты
    contacts = page.should_be_contacts()
    # link = contacts.get_attribute('href')

    # sbis_contacts: SbisContacts = SbisContacts(browser, link)
    # sbis_contacts.open()

    #Переходим в СБИС контакты
    contacts.click()


    # tensor_banner = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#contacts_clients a[href='https://tensor.ru/']")))

    sbis_contacts: SbisContacts = SbisContacts(browser, browser.current_url)

    tensor_banner = page.should_be_tensor_banner()
    # print(tensor_banner, tensor_banner.get_attribute('href'))
    # tensor_banner.click()

    tensor_page: TensorPage = TensorPage(browser, str(tensor_banner.get_attribute('href')))
    tensor_page.open()

    # try:
    #     # Tries to click an element
    #     sbis_contacts.should_be_tensor_banner().click()
    # except ElementClickInterceptedException:
    #     element = browser.find_element_by_class_name("sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm pl-20 pv-12 pl-xm-0 mt-xm-12")
    #     browser.execute_script("""
    #             var element = arguments[0];
    #             element.parentNode.removeChild(element);
    #             """, element)
    #Проверяем баннер Тензор
    # tensor_banner = sbis_contacts.should_be_tensor_banner()
    
    # print(f"!&{tensor_banner.get_attribute('href')}1&")
    # tensor_banner.click()

    # banner_url = None
    # if tensor_banner:
    #     banner_url = tensor_banner.get_attribute("href")
    # print(tensor_banner.text())
    # #Проходим на tensor.ru

    # banner_url = tensor_banner.get_attribute("href")

    # tensor_page: TensorPage = TensorPage(browser, browser.current_url)
    # tensor_page.open()


    # print(f"!!!!!{browser.current_url}!!!")

    #Проверяем, что мы на сайте tensor.ru
    tensor_page.should_be_tensor_url()
    #
    #Проверяем блок "Сила в людях"
    tensor_page.should_be_strength_in_people()

    #Проверяем блок "Подробнее"
    tensor_more_details = tensor_page.should_be_strength_in_people_more_details_link()

    browser.execute_script("arguments[0].scrollIntoView(true);", tensor_more_details)

    #Проходим на tensor more_details
    tensor_more_details.click()
    #
    tensor_more_details_page: TensorMoreDetails = TensorMoreDetails(browser, browser.current_url)

    # image = tensor_more_details_page.should_be_image_develop_sbis()
    #
    # print(image.size['height'])

    # #
    #Проверяем равномерности размеров изображений в разделе Работаем
    images_list = [
        tensor_more_details_page.should_be_image_develop_sbis(),
        tensor_more_details_page.should_be_image_promote_services(),
        tensor_more_details_page.should_be_image_create_infrastructure(),
        tensor_more_details_page.should_be_image_image_accompanying_clients()
        ]

    initial_height = images_list[0].size['height']
    initial_width = images_list[0].size['width']

    for image in images_list:
        assert image.size['height'] == initial_height, "Images height are not the same"
        assert image.size['width'] == initial_width, "Images width are not the same"





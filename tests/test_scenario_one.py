import time
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.sbis_contacts import SbisContacts
from pages.tensor_more_details import TensorMoreDetails


def test_scenario_one(browser):
    link = "https://sbis.ru/"
    page: SbisPage = SbisPage(browser, link)
    page.open()

    # Проверяем СБИС контакты
    contacts = page.should_be_contacts()

    # Переходим в СБИС контакты
    contacts.click()

    time.sleep(0.44)

    sbis_contacts: SbisContacts = SbisContacts(browser, browser.current_url)

    # time.sleep(0.44)

    # Проверяем tensor баннер и переходим на сайт tensor
    tensor_page: TensorPage = sbis_contacts.go_to_tensor()

    # time.sleep(0.44)

    # Проверяем, что мы на сайте tensor.ru
    tensor_page.should_be_tensor_url()

    # Проверяем блок "Сила в людях"
    tensor_page.should_be_strength_in_people()

    # Проверяем блок "Подробнее" и переходим на его страницу
    tensor_more_details_page: TensorMoreDetails = tensor_page.go_to_tensor_more_details()

    # Проверяем равномерности размеров изображений в разделе Работаем
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
from selenium.webdriver.common.by import By


class SBISLocators():
    SBIS_CONTASTS: tuple = (By.CSS_SELECTOR, ".sbisru-Header [href='/contacts']")


class SBISContactsLocators():
    BANNER_TENSOR: tuple = (By.CSS_SELECTOR, "#contacts_clients a[href='https://tensor.ru/']")
    MY_REGION: tuple = (By.CSS_SELECTOR,
                        "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span")
    LIST_PARTNERS: tuple = (
    By.CSS_SELECTOR, "#contacts_list > div > div.ws-flexbox.sbisru-Contacts-City__flex.sbisru-Contacts-Shot")
    REGION_KAMCHAT_KRAI: tuple = (By.CSS_SELECTOR,
                                  "#popup > div.controls-Popup.ws-float-area-show-complete.controls-Popup_shown.controls_themes__wrapper.controls-Scroll_webkitOverflowScrollingTouch.controls-Popup__lastItem > div > div > div > div > div.sbis_ru-Region-Panel.sbis_ru-Region-Panel-l > div > ul > li:nth-child(43) > span > span")


class TensorLocators():
    STRENGHT_IS_IN_PEOPLE_TEXT: tuple = (By.CSS_SELECTOR,
                                         "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p.tensor_ru-Index__card-title.tensor_ru-pb-16")
    STRENGHT_IS_IN_PEOPLE_MORE_DETAILS: tuple = (By.CSS_SELECTOR,
                                                 "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a")


class TensorMoreDetailsLocators():
    IMAGE_DEVELOP_SBIS: tuple = (By.CSS_SELECTOR,
                                 "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(1) > a > div.tensor_ru-About__block3-image-wrapper > img")

    IMAGE_CREATE_INFRASTRUCTURE: tuple = (By.CSS_SELECTOR,
                                          "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(3) > a > div.tensor_ru-About__block3-image-wrapper > img")
    IMAGE_ACCOMPANYING_CLIENT: tuple = (By.CSS_SELECTOR,
                                        "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(4) > a > div.tensor_ru-About__block3-image-wrapper > img")
    IMAGE_PROMOTE_SERVICES: tuple = (By.CSS_SELECTOR,
                                     "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(2) > a > div.tensor_ru-About__block3-image-wrapper > img")

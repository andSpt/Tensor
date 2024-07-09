from selenium.webdriver.common.by import By


class ProductPageLocators():
    SBIS_CONTASTS = (By.CSS_SELECTOR, ".sbisru-Header [href='/contacts']")
    BANNER_TENZOR = (By.CSS_SELECTOR,
                     "#contacts_clients > div.sbis_ru-container > div > div > div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 > div > a")
    STRENGHT_IS_IN_PEOPLE_TEXT = (By.CSS_SELECTOR,
                             "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p.tensor_ru-Index__card-title.tensor_ru-pb-16")
    STRENGHT_IS_IN_PEOPLE_MORE_DETAILS = (By.CSS_SELECTOR,
                                          "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a")
    IMAGE_DEVELOP_SBIS = (By.CSS_SELECTOR,
                          "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(1) > a > div.tensor_ru-About__block3-image-wrapper > img")  # container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(1) > a > div.tensor_ru-About__block3-image-wrapper > img
    IMAGE_PROMOTE_SERVICES = (By.CSS_SELECTOR,
                              "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(2) > a > div.tensor_ru-About__block3-image-wrapper > img")
    IMAGE_CREATE_INFRASTRUCTURE = (By.CSS_SELECTOR,
                                   "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(3) > a > div.tensor_ru-About__block3-image-wrapper > img")
    IMAGE_ACCOMPANYING_CLIENT = (By.CSS_SELECTOR,
                                 "#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.s-Grid-container > div:nth-child(4) > a > div.tensor_ru-About__block3-image-wrapper > img")


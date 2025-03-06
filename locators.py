from selenium.webdriver.common.by import By


class MainPageLocators:
    """Locators main page"""

    CONTACTS: tuple[str, str] = (By.CSS_SELECTOR, "ul.sbisru-Header__menu div.sbisru-Header__menu-link")
    CONTACTS_MORE: tuple[str, str] = (By.CSS_SELECTOR, "ul.sbisru-Header__menu a.sbisru-link.sbis_ru-link span")
    DOWNLOAD_LOCAL_VERSIONS: tuple[str, str] = (By.XPATH, "//a[text()='Скачать локальные версии']")


class SbisContactsLocators:
    """Locators contacts page"""

    BANNER_TENSOR: tuple[str, str] = (By.CSS_SELECTOR, "div#contacts_clients div.sbisru-Contacts__border-left img")
    REGION: tuple[str, str] = (By.CSS_SELECTOR, "div.sbis_ru-container.sbisru-Contacts__relative span span")
    LIST_PARTNERS: tuple[str, str] = (By.CSS_SELECTOR, "div#contacts_list div.sbisru-Contacts-List__col div[name='itemsContainer'] div#city-id-2")
    REGION_KAMCHATKA: tuple[str, str] = (By.XPATH, "//span[text()='41 Камчатский край']")


class TensorLocators:
    """Locators tensor page"""

    BLOCK_STRENGTH_IN_PEOPLE: tuple[str, str] = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content p:nth-of-type(1)")
    MORE_DETAILS: tuple[str, str] = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-bg p:nth-child(4) a")


class AboutLocators:
    """Locators about page"""

    IMG_DEV_SISTEM_SABY: tuple[str, str] = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(1) img")
    IMG_PROMOTE_SERVICES: tuple[str, str] = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(2) img")
    IMG_CREATE_INFRASTRUCTURE: tuple[str, str] = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(3) img")
    IMG_ASSIST_CLIENTS: tuple[str, str] = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-About__block3 div.s-Grid-container div.s-Grid-col:nth-of-type(4) img")


class DownloadSabyLocators:
    """Locators download Saby page"""

    SBIS_PLUGIN: tuple[str, str] = (By.XPATH, "//div[text()='Saby Plugin']")
    TAB_WINDOWS: tuple[str, str] = (By.XPATH, "//span[text()='Windows']")
    FILE_WINDOWS_DOWNLOAD_EXE: tuple[str, str] = (By.XPATH, "//a[contains(text(), 'Скачать (Exe')]")
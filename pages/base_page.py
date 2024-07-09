from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def is_element_present(self, how, what):
        try:
            obj = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return obj


#Получение элемента. Locator - атрибут класса из файла locators.py
    def get_element(self, Locator: tuple):
        return self.is_element_present(*Locator)

    def open(self):
        self.browser.get(self.url)



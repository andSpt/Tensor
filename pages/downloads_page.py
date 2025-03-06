from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators import DownloadSabyLocators


class DownloadsPage(BasePage):
    # def __init__(self, browser: WebDriver, url: str, timeout: int) -> None:
    #     super().__init__(browser, url, timeout)

    def should_be_sbis_plugin(self) -> WebElement:
        assert (sbis_plugin := self.is_element_present(DownloadSabyLocators.SBIS_PLUGIN)), "нет кнопки СБИС Плагин"
        return sbis_plugin

    def should_be_tab_windows(self) -> WebElement:
        assert (tab_windows := self.is_element_present(DownloadSabyLocators.TAB_WINDOWS)), "нет вкладки windows"
        return tab_windows

    def should_be_file_download_exe(self) -> WebElement:
        assert (file := self.is_element_present(DownloadSabyLocators.FILE_WINDOWS_DOWNLOAD_EXE)), "нет ссылки на файл"
        return file

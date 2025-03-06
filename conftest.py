from pathlib import Path
import pytest
import shutil

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


DOWNLOAD_DIR: Path = Path.cwd() / 'download/'

@pytest.fixture(scope='module')
def browser():
    chrome_options: Options = Options()
    chrome_options.add_experimental_option(
        "prefs", {
        "download.default_directory": str(DOWNLOAD_DIR),
        "download.prompt_for_download": False,
        "safebrowsing.allow_downloads_from_hosts": "https://sbis.ru/",
        "safebrowsing.enabled": True,
        "download.directory_upgrade": True,
    })
    browser: WebDriver = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def cleanup_download():
    if DOWNLOAD_DIR.is_dir():
        shutil.rmtree(str(DOWNLOAD_DIR))
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    yield
    shutil.rmtree(str(DOWNLOAD_DIR))


@pytest.fixture
def config_data():
    data: dict = {'path_to_dir_download': DOWNLOAD_DIR}
    return data


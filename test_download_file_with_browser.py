import time

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_download_file_with_browser():
    options = webdriver.ChromeOptions()
    download_folder = 'resources'
    prefs = {
        "download.default_directory": os.path.join(os.path.dirname(__file__), download_folder),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(10)

    downloaded_file_path = os.path.join(download_folder, 'pytest-main.zip')
    assert os.path.exists(downloaded_file_path), f"The file {downloaded_file_path} was not downloaded"

    file_size = os.path.getsize(downloaded_file_path)
    assert file_size > 0, f"The file {downloaded_file_path} is empty"

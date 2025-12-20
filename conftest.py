import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FFOption

def pytest_addoption(parser): # хук для запуска пайтеста

    parser.addoption('--browser', default='ch', help='Browser: ch (Chrome) or ff (Firefox)')
    parser.addoption('--headless', action='store_true', help='Run in headless mode')  # для запуска без UI
    parser.addoption('--url', default='http://localhost:8081', help='Base URL for tests')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')  # для запуска без UI
    base_url = request.config.getoption('--url')

    driver = None
    if browser_name == 'ch':
        option = ChromeOption()
        if headless:
            option.add_argument('--headless=new')
        driver = webdriver.Chrome(options=option)
    elif browser_name == 'ff':
        option = FFOption()
        if headless:
            option.add_argument('--headless')
        driver = webdriver.Firefox(options=option)
    else:
        raise ValueError(f'Driver for {browser_name} not supported')

    driver.maximize_window()

    driver.base_url = base_url

    yield driver

    driver.quit()

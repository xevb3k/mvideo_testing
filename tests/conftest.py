import pytest
from selenium import webdriver
import config


@pytest.fixture(scope='function')
def web_driver_desktop():
    """Фикстура инициализирует драйвер браузера, настраивает неявное время ожидания
       используемый браузер берется из конфигурации"""
    try:
        if config.DEFAULT_BROWSER == 'chrome':
            option = webdriver.ChromeOptions()
            option.add_argument("--disable-notifications")
            web_driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=option)
        elif config.DEFAULT_BROWSER == 'firefox':
            web_driver = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER_PATH)
        web_driver.maximize_window()
        web_driver.implicitly_wait(config.IMPLICITLY_WAIT_TIME)
        yield web_driver
    finally:
        web_driver.quit()


@pytest.fixture(scope='function')
def web_driver(browser, window_width, window_height):
    """Фикстура инициализирует драйвер браузера, настраивает неявное время ожидания
       используемый браузер и размеры окна получаем из параметров теста"""
    try:
        if browser == 'chrome':
            option = webdriver.ChromeOptions()
            option.add_argument("--disable-notifications")
            web_driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=option)
        elif browser == 'firefox':
            web_driver = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER_PATH)
        if window_width is None or window_height is None:
            web_driver.maximize_window()
        else:
            web_driver.set_window_size(window_width, window_height)
        web_driver.implicitly_wait(config.IMPLICITLY_WAIT_TIME)
        yield web_driver
    finally:
        web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_desktop_firefox():
    """Фикстура инициализирует драйвер браузера, настраивает неявное время ожидания
       Только FireFox в максимальном размере окна"""
    web_driver = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER_PATH)
    web_driver.maximize_window()
    web_driver.implicitly_wait(config.IMPLICITLY_WAIT_TIME)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_desktop_chrome():
    """Фикстура инициализирует драйвер браузера, настраивает неявное время ожидания
    Только Chrome в максимальном размере окна"""
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=option)
    web_driver.maximize_window()
    web_driver.implicitly_wait(config.IMPLICITLY_WAIT_TIME)
    yield web_driver
    web_driver.quit()
    
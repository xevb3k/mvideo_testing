import pytest
from selenium import webdriver
import config
import testdata


def browser_get_ids(browsers):
    return [f'{browser}' for browser in browsers]


def window_size_get_ids(window_sizes):
    return [f'{size[0]}x{size[1]}' for size in window_sizes]


@pytest.fixture(params=testdata.browsers_list, ids=browser_get_ids(testdata.browsers_list))
def browser(request):
    return request.param


@pytest.fixture(params=testdata.window_size_list, ids=window_size_get_ids(testdata.window_size_list))
def window_size(request):
    return request.param


@pytest.fixture(scope='function')
def web_driver_desktop():
    """Фикстура инициализирует драйвер браузера, настраивает неявное время ожидания
       используемый браузер берется из конфигурации"""
    web_driver = None
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
def web_driver(browser, window_size):
    """Фикстура инициализирует драйвер браузера, настраивает неявное время ожидания
       используемый браузер и размеры окна получаем из фикстур browser, window_size"""
    web_driver = None
    try:
        if browser == 'chrome':
            option = webdriver.ChromeOptions()
            option.add_argument("--disable-notifications")
            web_driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=option)
        elif browser == 'firefox':
            web_driver = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER_PATH)
        if window_size[0] is None or window_size[1] is None:
            web_driver.maximize_window()
        else:
            web_driver.set_window_size(window_size[0], window_size[1])
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
    
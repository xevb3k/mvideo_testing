import pytest
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from pages.site_params import MVideoLinks
from pages.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.positive
def test_link_all_stocks(web_driver_desktop):
    """Тест проверяет переход по ссылке "Все акции" """
    page = HomePage(web_driver_desktop)
    page.main_menu_link_all_stocks.click()
    page.wait_page_loaded()
    assert page.get_relative_link() == MVideoLinks.link_home_page_main_menu_all_stocks


@pytest.mark.smoke
@pytest.mark.positive
def test_products_of_day_block(web_driver_desktop):
    """Тест проверяет, что на странице присутствует блок "Товары дня"  """
    page = HomePage(web_driver_desktop)
    page.wait_page_loaded()
    
    day_products_block = page.x_day_products_block
    day_products_block_text = page.x_day_products_block_text
    assert len(day_products_block) != 0 and len(day_products_block_text) != 0
    

@pytest.mark.smoke
@pytest.mark.positive
def test_products_of_day_link(web_driver_desktop):
    """Тест проверяет, что у всех товаров дня есть ссылка  """
    page = HomePage(web_driver_desktop)
    page.wait_page_loaded()

    day_products = page.x_day_products
    day_products_link = page.x_day_products_img
    assert len(day_products) == len(day_products_link)
    
    for prod in day_products_link:
        assert prod.get_attribute('href') != ''


@pytest.mark.smoke
@pytest.mark.positive
def test_all_stocks_have_img_url(web_driver_desktop):
    """Тест проверяет, что у всех акций на странице ВСЕ АКЦИИ есть изображение и url"""
    page = HomePage(web_driver_desktop)
    page.main_menu_link_all_stocks.click()
    page.wait_page_loaded()
    stock_list = page.x_all_stocks_list
    stock_img_list = page.x_all_stocks_img_list
    all_stock_have_img = True
    all_stock_have_url = True
    for stock in stock_img_list:
        if len(stock.get_attribute('src')) == 0:
            all_stock_have_img = False
            break
    for stock in stock_list:
        if len(stock.get_attribute('href')) == 0:
            all_stock_have_url = False
            break
    assert len(stock_list) == len(stock_img_list) and all_stock_have_img and all_stock_have_url


@pytest.mark.smoke
@pytest.mark.positive
def test_all_stocks_compare_url(web_driver_desktop):
    """Тест проверяет, что у всех акций на странице "ВСЕ АКЦИИ" url на изображении совпадает с url на названии акции"""
    page = HomePage(web_driver_desktop)
    page.main_menu_link_all_stocks.click()
    page.wait_page_loaded()
    stock_list = page.x_all_stocks_list
    stock_name_list = page.x_all_stocks_name_list
    assert len(stock_list) == len(stock_name_list)
    
    for stock, stock_name in zip(stock_list, stock_name_list):
        if stock.get_attribute('href') != stock_name.get_attribute('href'):
            assert False
    assert True


@pytest.mark.smoke
@pytest.mark.positive
def test_all_stocks_have_name(web_driver_desktop):
    """Тест проверяет, что у всех акций на странице "ВСЕ АКЦИИ" есть название"""
    page = HomePage(web_driver_desktop)
    page.main_menu_link_all_stocks.click()
    page.wait_page_loaded()
    stock_name_list = page.x_all_stocks_name_list
    for stock in stock_name_list:
        print(stock.text)
        if stock.text.replace(' ', '') == '':
            assert False
    assert True


@pytest.mark.smoke
@pytest.mark.positive
def test_all_stocks_have_desc(web_driver_desktop):
    """Тест проверяет, что у всех акций на странице "ВСЕ АКЦИИ" есть краткое описание"""
    page = HomePage(web_driver_desktop)
    page.main_menu_link_all_stocks.click()
    page.wait_page_loaded()
    stock_desc_list = page.x_all_stocks_desc_list
    for stock in stock_desc_list:
        print(stock.text)
        if stock.text.replace(' ', '') == '':
            assert False, 'не у всех акций на странице "Все акции" есть крат.описание'
    assert True
    
import pytest
import sys
import random
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from pages.home_page import HomePage
from pages.site_params import MVideoLinks
from tests.testdata import *


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("browser", test_browsers)
@pytest.mark.parametrize("window_width, window_height", window_size_list)
def test_homepage_is_opened(web_driver, window_width, window_height):
    """Тест проверяет загрузку главной страницы в различных браузерах и с различными размерами окна"""
    page = HomePage(web_driver)
    page.wait_page_loaded()
    assert page.driver.current_url == MVideoLinks.home_page_url, error_test_homepage_is_opened
   
   
@pytest.mark.smoke
@pytest.mark.positive
def test_logo_click(web_driver_desktop):
    """Тест проверяет загрузку главной страницы при клике на логотип"""
    page = HomePage(web_driver_desktop)
    page.logo_img.click()
    assert page.driver.current_url == MVideoLinks.home_page_url, error_test_logo_click


@pytest.mark.smoke
@pytest.mark.positive
def test_link_blog_m_click(web_driver_desktop):
    """Тест проверяет переход по ссылке "Блог М.Клик" """
    page = HomePage(web_driver_desktop)
    page.link_blog_m_click.click()
    assert page.get_relative_link() == MVideoLinks.link_home_page_blog_m_click, error_test_link_blog_m_click


@pytest.mark.smoke
@pytest.mark.positive
def test_link_m_club(web_driver_desktop):
    """Тест проверяет переход по ссылке "M.Club" """
    page = HomePage(web_driver_desktop)
    page.link_m_club.click()
    assert page.get_relative_link() == MVideoLinks.link_home_page_m_club, error_test_link_m_club


@pytest.mark.smoke
@pytest.mark.positive
def test_link_for_business(web_driver_desktop):
    """Тест проверяет переход по ссылке "Для бизнеса" """
    page = HomePage(web_driver_desktop)
    page.link_for_business.click()
    assert page.get_relative_link() == MVideoLinks.link_home_page_for_business, error_test_link_for_business
  

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_positive(web_driver_desktop, search_text):
    """Тест проверяет работу поиска с разными данными """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_for_products_loaded()
    assert len(page.x_search_result_product_list_block) > 0 and len(page.x_text_search_result_not_found) == 0
    

@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.parametrize("search_text", search_negative[0], ids=search_negative[1])
def test_search_negative(web_driver_desktop, search_text):
    """Тест проверяет работу поиска с разными негативными данными """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    assert len(page.x_search_result_product_list_block) == 0 and len(page.x_text_search_result_not_found) > 0


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_have_image(web_driver_desktop, search_text):
    """Тест проверяет, что у всех найденных товаров есть фото """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_for_products_loaded()
    product_list = page.x_search_product_list
    product_image_list = page.x_search_product_image_list
    assert len(product_list) == len(product_image_list)


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_have_button_to_cart(web_driver_desktop, search_text):
    """Тест проверяет, что у всех найденных товаров есть кнопка "Добавить в корзину" и кнопка кликабельна """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    product_list = page.x_search_product_list
    product_button_to_cart_list = page.x_search_product_button_to_cart_list
    product_button_analogs_list = page.x_search_product_button_analogs_list
    print(len(product_button_to_cart_list), len(product_button_analogs_list))
    all_buttons_enabled = True
    for prod in product_button_to_cart_list:
        if not prod.is_enabled():
            all_buttons_enabled = False
            break
    assert len(product_list) == len(product_button_to_cart_list) + len(product_button_analogs_list) \
           and all_buttons_enabled


# на 30.08.22 тут баг - бабл не обновляется сразу после добавления товара в корзину
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_add_to_cart(web_driver_desktop, search_text):
    """Тест проверяет, что случайное количество товаров из результатов поиска, положенных в корзину, равно количеству,
       указанному на баббле над корзиной.
       А также, что такое же количество кнопок "В корзину" изменило свое название на "В корзине" """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_for_products_loaded()
    product_button_to_cart_list = page.x_search_product_button_to_cart_list
    
    # добавляем случайное количество в корзину в случайном порядке
    random.shuffle(product_button_to_cart_list)
    cnt = 0
    for prod in product_button_to_cart_list[:random.randint(1, len(product_button_to_cart_list))]:
        prod.click()
        cnt += 1
        # ожидание минимум 1.5 секунды - время сокрытия всплывающей корзины
        page.wait_page_loaded(sleep_time=1.5)
    
    product_button_in_cart_list = page.x_search_product_button_in_cart_list
    assert int(page.cart_count_bubble.text) == len(product_button_in_cart_list) == cnt


def get_int_price_list(objects_list_contain_price):
    """ На основании списка объектов страницы, содержащих цены продуктов, формирует список цен в int формате """
    return [int(price.text.replace(' ', '').replace('₽', '')) for price in objects_list_contain_price]


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_sort_low_price(web_driver_desktop, search_text):
    """Тест проверяет работу сортировки товар после поиска от дешевых к дорогим  """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_for_products_loaded()

    page.search_product_list_sort_price_popular_before.click()
    page.search_product_list_sort_price_low_before_popup.click()
    page.wait_for_products_loaded()
    price_list = get_int_price_list(page.x_search_products_price)
    
    assert price_list == sorted(price_list), 'некорректная сортировка по цене от дешевых'


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_sort_high_price(web_driver_desktop, search_text):
    """Тест проверяет работу сортировки товара после поиска от дорогих к дешевым  """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    
    page.search_product_list_sort_price_popular_before.click()
    page.search_product_list_sort_price_high_before_popup.click()
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    price_list = get_int_price_list(page.x_search_products_price)
    
    assert price_list == sorted(price_list, reverse=True), 'некорректная сортировка по цене от дорогих'


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
@pytest.mark.parametrize("min_value", price_min_value)
@pytest.mark.parametrize("max_value", price_max_value)
def test_search_products_min_max_price(web_driver_desktop, search_text, min_value, max_value):
    """Тест проверяет работу фильтра по максимальной/минимальной цене:
    1. Ищем определенные товары
    2. Заносим в фильтр мин/макс цены
    3. Проверяем, есть ли среди найденных товаров товары с ценами за границами фильтра
    Тест учитывает мин/макс значения, которые система позволит внести в фильтр """
    
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_page_loaded()
    page.wait_for_products_loaded()

    input_min_value = page.search_product_list_input_min_price
    input_max_value = page.search_product_list_input_max_price
    
    real_min_price = input_min_value.get_attribute('placeholder').replace(' ', '')
    real_max_price = input_max_value.get_attribute('placeholder').replace(' ', '')

    if int(max_value) < int(min_value):
        max_value = min_value
    if int(min_value) < int(real_min_price) and int(max_value) < int(real_min_price):
        min_value = real_min_price
        max_value = real_min_price
    elif int(min_value) < int(real_min_price) and int(max_value) > int(real_max_price):
        min_value = real_min_price
        max_value = real_max_price
    elif int(min_value) > int(real_max_price) and int(max_value) > int(real_max_price):
        min_value = real_max_price
        max_value = real_max_price
    elif int(min_value) < int(real_min_price) and int(max_value) >= int(real_min_price) and int(max_value) <= int(real_max_price):
        min_value = real_min_price
    elif int(min_value) >= int(real_min_price) and int(min_value) <= int(real_max_price) and int(max_value) > int(real_max_price):
        max_value = real_max_price

    page.input_field_put_value(input_min_value, min_value)
    page.input_field_put_value(input_max_value, max_value)
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    
    price_list = get_int_price_list(page.x_search_products_price)
    if len(price_list) > 0:
        assert min(price_list) >= int(min_value) and max(price_list) <= int(max_value)
    else:
        # если товары по данному фильтру не найдены, тест не считать упавшим
        assert True


# на 30.08.22 тут баги - подсказки очень часто нерелевантны найденным товарам
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_min_max_prompt(web_driver_desktop, search_text):
    """Тест проверяет корректность подсказок в фильтре в полях мин/макс цены:
    1. Ищем определенный товар
    2. Проверяем, что подсказки в фильтре мин/макс соответствуют мин/макс ценам среди найденных товаров
     """
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    prompt_min_price = int(page.search_product_list_input_min_price.get_attribute('placeholder').replace(' ', ''))
    prompt_max_price = int(page.search_product_list_input_max_price.get_attribute('placeholder').replace(' ', ''))
    
    page.search_product_list_sort_price_popular_before.click()
    page.search_product_list_sort_price_high_before_popup.click()
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    max_price = get_int_price_list(page.x_search_products_price)[0]
   
    page.search_product_list_sort_price_high_before.click()
    page.search_product_list_sort_price_low_before_popup.click()
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    min_price = get_int_price_list(page.x_search_products_price)[0]
    assert prompt_min_price == min_price and prompt_max_price == max_price


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_with_discount_have_sale_price(web_driver_desktop, search_text):
    """Тест проверяет, что у товаров со скидкой есть доп. цена до скидки"""
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    products_with_discount = page.x_products_with_discount_checkbox
    if products_with_discount:
        products_with_discount[0].click()
        page.wait_page_loaded()
        page.wait_for_products_loaded()
        product_list = page.x_search_product_list
        product_with_sale_price = page.x_search_products_price_sale
        product_list_analog = page.x_search_product_button_analogs_list
        assert len(product_list) == len(product_with_sale_price) + len(product_list_analog)
    else:
        # если товары по данному фильтру не найдены, тест не считать упавшим
        assert True


# здесь на 25.08.22 баг - система дает поставить в поле макс цену больше предполагамемой максимальной
# но не напрямую, а через внесение такой цены в поле мин
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("search_text", search_positive[0], ids=search_positive[1])
def test_search_products_filter_min_max(web_driver_desktop, search_text):
    """Тест проверяет, что нельзя установить в фильтр мин/макс цены меньше или больше тех, что в подсказках """
    
    page = HomePage(web_driver_desktop)
    page.input_field_put_value(page.search_field, search_text)
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    input_min_value = page.search_product_list_input_min_price
    input_max_value = page.search_product_list_input_max_price
    prompt_min_price = input_min_value.get_attribute('placeholder').replace(' ', '')
    prompt_max_price = input_max_value.get_attribute('placeholder').replace(' ', '')
    print(prompt_min_price, prompt_max_price)
    
    # пробуем поставить цены меньше минимальной и больше максимальной
    page.input_field_put_value(input_min_value, str(int(prompt_min_price)-1))
    page.input_field_put_value(input_max_value, str(int(prompt_max_price)+1))
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    min_price = input_min_value.get_attribute('value').replace(' ', '')
    max_price = input_max_value.get_attribute('value').replace(' ', '')
    print(min_price, max_price)
    assert prompt_min_price == min_price and prompt_max_price == max_price
    
    # пробуем поставить в поле макс цену меньше минимально допустимой
    page.input_field_put_value(input_max_value, str(int(prompt_min_price)-1))
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    min_price = input_min_value.get_attribute('value').replace(' ', '')
    max_price = input_max_value.get_attribute('value').replace(' ', '')
    assert prompt_min_price == min_price and prompt_min_price == max_price
    
    # пробуем поставить в поле мин цену больше максимально допустимой
    # здесь на 25.08.22 баг - система дает поставить в поле макс цену больше предполагамемой максимальной
    # но не напрямую, а через внесение такой цены в поле мин
    page.input_field_put_value(input_min_value, str(int(prompt_max_price)+1))
    page.wait_page_loaded()
    page.wait_for_products_loaded()
    min_price = input_min_value.get_attribute('value').replace(' ', '')
    max_price = input_max_value.get_attribute('value').replace(' ', '')
    assert prompt_max_price == min_price and prompt_max_price == max_price, error_test_search_products_filter_min_max
    
    
@pytest.mark.smoke
@pytest.mark.positive
def test_catalog(web_driver_desktop):
    """Тест проверяет раскрытие меню Каталог с главной страницы и после перехода в случайную категорию"""
    page = HomePage(web_driver_desktop)
    page.button_catalog.click()
    catalog1 = page.x_catalog_categories
    if not catalog1:
        assert False, error_test_catalog
    else:
        random.shuffle(catalog1)
        catalog1[0].click()
        page.wait_page_loaded()
        page.button_catalog2.click()
        catalog2 = page.x_catalog_categories2
        if not catalog2:
            assert False, error_test_catalog
        else:
            assert True
                
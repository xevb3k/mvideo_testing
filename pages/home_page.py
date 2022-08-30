from time import sleep
from pages.base_page import BasePage
from pages.locators import HomePageLocators
from pages.site_params import MVideoLinks
from pages.site_params import MVideoSiteParam
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, MVideoLinks.home_page_url)
        if self.width <= MVideoSiteParam.window_width_mobile_max:
            self.site_version = 'mobile'
        elif self.width <= MVideoSiteParam.window_width_tablet_max:
            self.site_version = 'tablet'
        else:
            self.search_field_put_value = 'desktop'
        self.driver.get(self.url)
 
    def __getattribute__(self, item):
        """ Поиск элемента производится каждый раз при обращении к атрибуту
            Локатор берем из словаря (ключ - атрибут)
            Если имя атрибута (локатора) начинается на x_ то применяется поиск нескольких элементов find_elements """
        get_several_elem = str(item).startswith('x_')
        if get_several_elem:
            item = item[2:]
        elem = HomePageLocators.elements.get(item)
        if elem:
            if get_several_elem:
                return self.driver.find_elements(*elem)
            else:
                return self.driver.find_element(*elem)
        else:
            return super().__getattribute__(item)

    def search_field_put_value(self, search_value):
        """ Ввод значения в поле поиска """
        search_field = self.search_field
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.send_keys(Keys.ENTER)

    @staticmethod
    def input_field_put_value(field, value):
        field.clear()
        field.send_keys(value)
        field.send_keys(Keys.ENTER)

    def wait_for_products_loaded(self):
        #while self.x_skeleton_listing or self.x_product_cards_layout_loading:
        while 'class="product-cards-layout product-cards-layout--grid product-cards-layout--loading"' in self.driver.page_source\
                or 'mvid-skeleton-listing' in self.driver.page_source:
            pass
        
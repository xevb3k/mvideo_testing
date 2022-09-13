from pages.site_params import MVideoSiteParam
from pages.gen_methods import StringGenMethods


search_positive = (['чайник', 'пылесос', 'чайник со свистком', 'телевизор с 3D'],
                   ['ru', 'ru2', 'more_ru', 'ru_en_num'])

search_negative = ([StringGenMethods.generate_string(255), StringGenMethods.generate_string(1001),
                    StringGenMethods.russian_chars(), StringGenMethods.russian_chars().upper(),
                    StringGenMethods.english_chars(), StringGenMethods.special_chars()],
                   ['255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'english', 'specials'])

price_min_value = ['100', '999', '1000', '49999']
price_max_value = ['500', '4999', '99999']

browsers_list = ['chrome', 'firefox']

window_width_mobile_avg = MVideoSiteParam.window_width_mobile_max // 2
window_width_tablet_avg = (MVideoSiteParam.window_width_tablet_max -
                           MVideoSiteParam.window_width_tablet_min) // 2 + \
                           MVideoSiteParam.window_width_tablet_min
window_width_desktop_avg = (MVideoSiteParam.window_width_desktop_max -
                            MVideoSiteParam.window_width_desktop_min) // 2 + \
                            MVideoSiteParam.window_width_desktop_min

# width "None" - maximize window (height ignored)
window_size_list = [(window_width_desktop_avg, MVideoSiteParam.window_default_height),
                    (window_width_tablet_avg, MVideoSiteParam.window_default_height),
                    (window_width_mobile_avg, MVideoSiteParam.window_default_height)]


error_test_homepage_is_opened = 'главная страница не загружена'
error_test_logo_click = 'при клике на логотип не происходит переход на главную страницу'
error_test_link_blog_m_click = 'ошибка при клике на ссылку "Блог М.Клик"'
error_test_link_m_club = 'ошибка при клике на ссылку "M.Club"'
error_test_link_for_business = 'ошибка при клике на ссылку "Для бизнеса"'
error_test_search_products_filter_min_max = 'система дает внести в поле фильтра макс цену больше максимальной предполагаемой'
error_test_catalog = 'Каталог не раскрыт'
error_test_all_stocks_have_desc = 'не у всех акций на странице "Все акции" есть крат.описание'
error_test_all_stocks_have_name = 'не у всех акций на странице "Все акции есть название'
error_test_all_stocks_compare_url = 'не у всех акций на странице "ВСЕ АКЦИИ" url на изображении совпадает с url на названии акции'
error_test_all_stocks_have_img_url = 'не у всех акций на странице ВСЕ АКЦИИ есть изображение и url'
error_test_products_of_day_link = 'не у всех товаров дня есть ссылка'
error_test_products_of_day_block = 'на странице отстутствует блок "Товары дня"'
error_test_link_all_stocks = 'оишбка при переходе по ссылке "Все акции"'

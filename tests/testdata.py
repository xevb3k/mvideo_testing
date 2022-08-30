from pages.site_params import MVideoSiteParam


search_positive = (['смартфоны', 'телевизор с 3D', 'iphone'],
                   ['ru', 'more_ru', 'eng'])

test_browsers = ['chrome', 'firefox']

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


error_main_page_not_loaded = 'главная страница не загружена'

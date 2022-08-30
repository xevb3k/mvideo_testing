from selenium.webdriver.common.by import By


class HomePageLocators:

    elements = {'logo_img': (By.CSS_SELECTOR, 'img.ng-tns-c224-1'),
                'link_main_page': (By.XPATH, '//a[@href="https://www.mvideo.ru/" or @href="/"]'),
                'link_blog_m_click': (By.XPATH, '//a[text()="Блог «М.Клик»"]'),
                'link_m_club': (By.XPATH, '//a[text()="M.Club"]'),
                'link_for_business': (By.XPATH, '//a[text()="Для бизнеса"]'),
                'main_menu_link_all_stocks': (By.XPATH, '//a[text()="ВСЕ АКЦИИ"]'),

                # список товаров дня
                'day_products': (By.CSS_SELECTOR, 'mvid-day-products-block mvid-day-product'),
                'day_products_img': (By.CSS_SELECTOR, 'div.carousel mvid-day-product a.image img'),
                'day_products_link': (By.CSS_SELECTOR, 'div.carousel mvid-day-product a.image'),
                
                'day_products_block': (By.CSS_SELECTOR, 'mvid-day-products-block'),
                'day_products_block_text': (By.XPATH, '//mvid-day-products-block/div/mvid-title-timer/div/div/span[text()="Товары дня"]'),
                # активный товар дня
                'day_products_main': (By.CSS_SELECTOR, 'div.carousel div.product-container mvid-day-product.product.main'),
                
                'all_stocks_list': (By.CSS_SELECTOR, 'a.lazy-load-image-holder'),
                'all_stocks_img_list': (By.CSS_SELECTOR, 'div.c-preview-article__img-wrap a div img'),
                'all_stocks_name_list': (By.CSS_SELECTOR, 'a.c-preview-article__title-link'),
                'all_stocks_desc_list': (By.CSS_SELECTOR, 'div.c-preview-article__text '),
                # поле поиска
                'search_field': (By.CSS_SELECTOR, 'input.input__field'),
                # блок с карточками товаров после поиска
                'search_result_product_list_block': (By.CSS_SELECTOR, 'mvid-product-list-block'),
                # если поиск неудачный - элемент с текстом "По вашему запросу ничего не найдено"
                'text_search_result_not_found': (By.XPATH, '//p[text()="По вашему запросу ничего не найдено"]'),
                # список - карточки товаров в результате поиска
                'search_product_list': (By.CSS_SELECTOR, 'mvid-plp-product-picture.product-card__picture.ng-star-inserted'),
                # список - фото товаров в результате поиска
                'search_product_image_list': (By.XPATH, '//mvid-plp-product-picture/div/div[1]/a/picture/img'),
                # список - кнопки "В корзину" в карточках товаров в результате поиска
                'search_product_button_to_cart_list': (By.XPATH, '//span[text()="В корзину"]'),
                # список - кнопки "Аналоги" в карточках товаров в результате поиска
                'search_product_button_analogs_list': (By.XPATH, '//button[text()=" Аналоги "]'),
                # список - кнопки "В корзине" в карточках товаров в результате поиска
                'search_product_button_in_cart_list': (By.XPATH, '//span[text()="В корзине"]'),
                # баббл над корзиной
                'cart_count_bubble': (By.CSS_SELECTOR, 'mvid-bubble.bubble.ng-star-inserted'),
                # список - цены продуктов в результате поиска
                'search_products_price': (By.CSS_SELECTOR, 'span.price__main-value'),
                # список - цены продуктов без скидки результате поиска
                'search_products_price_sale': (By.CSS_SELECTOR, 'span.price__sale-value.ng-star-inserted'),
                # ссылка выбора метода сортировки в результате поиска
                'search_product_list_sort_price_popular_before': (By.XPATH, '//span[text()="Сначала популярные"]'),
                'search_product_list_sort_price_low_before_popup': (By.XPATH, '//div[text()=" Сначала дешевле "]'),
                'search_product_list_sort_price_low_before': (By.XPATH, '//span[text()="Сначала дешевле"]'),
                'search_product_list_sort_price_high_before_popup': (By.XPATH, '//div[text()=" Сначала дороже "]'),
                'search_product_list_sort_price_high_before': (By.XPATH, '//span[text()="Сначала дороже"]'),
                # поля фильтра мин/макс цена
                'search_product_list_input_min_price': (By.CSS_SELECTOR, 'input[name="minPrice"]'),
                'search_product_list_input_max_price': (By.CSS_SELECTOR, 'input[name="maxPrice"]'),
                # чекбокс "Товары со скидкой", нулевой в списке
                'products_with_discount_checkbox': (By.CSS_SELECTOR, 'label.switcher.switcher--reversed'),
                
                # кнопка Каталог на главной
                'button_catalog': (By.CSS_SELECTOR, 'button.button.button--with-icon.ng-star-inserted'),
                # кнопка Каталог после перехода в каталог
                'button_catalog2': (By.CSS_SELECTOR, '.header-main__catalog-btn-text'),
                # список - левое меню категорий каталога
                'catalog_categories': (By.CSS_SELECTOR, 'a.left-menu__item-text'),
                'catalog_categories2': (By.CSS_SELECTOR, 'a.c-link.c-link_text.header-catalog__category.header-catalog__category'),
                
                # список - пока хоть один из элементов присутствует на странице - продукты не загружены
                'skeleton_listing': (By.CSS_SELECTOR, 'mvid-skeleton-listing'),
                # подложка для загружающихся продуктов
                'product_cards_layout_loading': (By.CSS_SELECTOR, 'div.product-cards-layout.product-cards-layout--grid.product-cards-layout--loading')
                }
    
    text_products_loading = 'class="product-cards-layout product-cards-layout--grid product-cards-layout--loading"',
    text_products_grid_loading = 'mvid-skeleton-listing'
    
    
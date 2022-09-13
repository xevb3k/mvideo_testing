Функциональное тестирование интернет-магазина МВидео.
Страница сайта интернет-магазина: https://www.mvideo.ru/


Этот репозиторий содержит автотесты сайта интернет-магазина МВидео.
Тесты выполнены на Python 3.9 с применением PageObject и фреймворков Pytest и Selenium.
Тесты запускаются в браузере Chrome и/или Firefox.
Каждый тест можно провести в любом из браузеров и с любым макетом страницы (desktop, tablet, mobile).

Файлы.
В каталоге tests находятся автотесты для тестируемых страниц магазина + тестовые данные.
В папке pages находятся файлы с классами и методами для работы с соответствующими страницами сайта, описаниями url сайта и вспомогательными методами.

Как запускать тесты:

Установить зависимости:
pip3 install -r requirements

Скачать Selenium Chrome WebDriver с https://chromedriver.chromium.org/downloads
Скачать Selenium Gecko WebDriver с https://github.com/mozilla/geckodriver/releases
Путь до скачанных файлов указать в файле config.py

Запустить тесты можно:
из среды разработки PyCharm все тесты, создав тестовую конфигурацию pytest и указав папку tests
из среды разработки PyCharm как отдельными тестами, так и одним файлом теста
из командной строки как файл теста, так и отдельный тест в файле:
pytest -v <test_file_name>::<test_name>

Команды для запуска тестов:
python -m pytest -v --driver <driver_name> --driver-path <driverpath> /tests/<test_file_name.py>

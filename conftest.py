import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import Urls


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для запуска браузера Firefox.

    Каждый тест получает новую сессию браузера.
    После теста браузер закрывается автоматически.
    """
    # Настройка опций браузера
    options = Options()
    
    # Создание драйвера
    driver = webdriver.Firefox(options=options)
    driver.get(Urls.BASE_URL)
    driver.maximize_window()

    yield driver

    driver.quit()
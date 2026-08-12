from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from locators.main_page_locators import MainPageLocators


class MainPage:
    """Page Object для главной страницы."""

    def __init__(self, driver):
        """Инициализация страницы."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_order_button_header(self):
        """Клик по кнопке «Заказать» в шапке страницы."""
        button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def click_order_button_middle(self):
        """Клик по кнопке «Заказать» в середине страницы."""
        # Прокручиваем вниз, чтобы кнопка стала видимой
        self.driver.execute_script("window.scrollTo(0, 500);")
        
        button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_MIDDLE)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", 
            button
        )
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", button)

    def click_question_button(self, index):
        """
        Клик по кнопке вопроса в блоке «Вопросы о важном».

        Args:
            index: Порядковый номер вопроса (0-based).
        """
        # Ждём все элементы аккордеона
        items = self.wait.until(
            EC.visibility_of_all_elements_located(MainPageLocators.QUESTION_ITEMS)
        )

        # Внутри элемента находим кнопку
        button = items[index].find_element(*MainPageLocators.QUESTION_BUTTON)

        # Прокручиваем к элементу с плавной анимацией
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", 
            button
        )
        
        # Небольшая пауза для завершения прокрутки
        time.sleep(0.5)
        
        # Кликаем через JavaScript для обхода перекрытия
        self.driver.execute_script("arguments[0].click();", button)

    def get_question_answer_text(self, index):
        """
        Получить текст ответа на вопрос.

        Args:
            index: Порядковый номер вопроса (0-based).

        Returns:
            Текст ответа в виде строки.
        """
        # Ждём все элементы аккордеона
        items = self.wait.until(
            EC.visibility_of_all_elements_located(MainPageLocators.QUESTION_ITEMS)
        )

        # Находим панель
        panel = items[index].find_element(*MainPageLocators.QUESTION_PANEL)
        # Ждём, пока панель станет видимой (после клика)
        self.wait.until(EC.visibility_of(panel))
        return panel.text

    def click_scooter_logo(self):
        """Клик по логотипу «Самокат» — переход на главную страницу."""
        logo = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)
        )
        self.driver.execute_script("arguments[0].click();", logo)

    def click_yandex_logo(self):
        """Клик по логотипу «Яндекс» — открытие Дзена в новой вкладке."""
        logo = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        self.driver.execute_script("arguments[0].click();", logo)

    def switch_to_new_window(self):
        """
        Переключиться на новую вкладку браузера.

        Returns:
            Handle исходной вкладки.
        """
        self.wait.until(EC.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        return original_window

    def wait_for_url_contains(self, expected_url_part: str):
        """
        Дождаться, пока URL текущей вкладки не будет содержать указанную подстроку.

        Args:
            expected_url_part: Часть ожидаемого URL (например, "dzen.ru").
        """
        self.wait.until(
            lambda driver: expected_url_part in driver.current_url
        )

    def switch_to_window(self, window_handle):
        """Переключиться на вкладку с указанным handle."""
        self.driver.switch_to.window(window_handle)

    def get_current_url(self) -> str:
        """Получить текущий URL страницы."""
        return self.driver.current_url
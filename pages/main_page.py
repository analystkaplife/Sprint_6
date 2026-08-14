from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import time


class MainPage(BasePage):
    """Page Object для главной страницы."""

    def click_order_button_header(self):
        """Клик по кнопке «Заказать» в шапке страницы."""
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_middle(self):
        """Клик по кнопке «Заказать» в середине страницы."""
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        time.sleep(0.3)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_MIDDLE)

    def click_question_button(self, index):
        """
        Клик по кнопке вопроса в блоке «Вопросы о важном».

        Args:
            index: Порядковый номер вопроса (0-based).
        """
        items = self.wait.until(
            self.EC.visibility_of_all_elements_located(MainPageLocators.QUESTION_ITEMS)
        )

        button = items[index].find_element(*MainPageLocators.QUESTION_BUTTON)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            button
        )
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", button)

    def get_question_answer_text(self, index):
        """
        Получить текст ответа на вопрос.

        Args:
            index: Порядковый номер вопроса (0-based).

        Returns:
            Текст ответа в виде строки.
        """
        items = self.wait.until(
            self.EC.visibility_of_all_elements_located(MainPageLocators.QUESTION_ITEMS)
        )

        panel = items[index].find_element(*MainPageLocators.QUESTION_PANEL)
        self.wait.until(self.EC.visibility_of(panel))
        return panel.text

    def click_scooter_logo(self):
        """Клик по логотипу «Самокат» — переход на главную страницу."""
        self.click_element_with_wait(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Клик по логотипу «Яндекс» — открытие Дзена в новой вкладке."""
        self.click_element_with_wait(MainPageLocators.YANDEX_LOGO)

    def get_current_url(self) -> str:
        """Получить текущий URL страницы."""
        return self.driver.current_url

    def switch_to_new_window(self):
        """
        Переключиться на новую вкладку браузера.

        Returns:
            Handle исходной вкладки.
        """
        self.wait.until(self.EC.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        return original_window

    def switch_to_window(self, window_handle):
        """Переключиться на вкладку с указанным handle."""
        self.driver.switch_to.window(window_handle)

    def wait_for_url_contains(self, expected_url_part: str):
        """
        Дождаться, пока URL текущей вкладки не будет содержать указанную подстроку.

        Args:
            expected_url_part: Часть ожидаемого URL (например, "dzen.ru").
        """
        self.wait.until(
            lambda driver: expected_url_part in driver.current_url
        )
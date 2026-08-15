import allure
import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Page Object для главной страницы."""

    @allure.step("Клик по кнопке «Заказать» в шапке страницы")
    def click_order_button_header(self):
        """Клик по кнопке «Заказать» в шапке страницы."""
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Клик по кнопке «Заказать» в середине страницы")
    def click_order_button_middle(self):
        """Клик по кнопке «Заказать» в середине страницы."""
        self.scroll_to_pixels(500)
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        time.sleep(0.3)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Клик по кнопке вопроса с индексом {index}")
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
        self.scroll_to_element_with_web_element(button)
        time.sleep(0.5)
        self.click_element_with_web_element(button)

    @allure.step("Получение текста ответа на вопрос с индексом {index}")
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

    @allure.step("Клик по логотипу «Самокат»")
    def click_scooter_logo(self):
        """Клик по логотипу «Самокат» — переход на главную страницу."""
        self.click_element_with_wait(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу «Яндекс»")
    def click_yandex_logo(self):
        """Клик по логотипу «Яндекс» — открытие Дзена в новой вкладке."""
        self.click_element_with_wait(MainPageLocators.YANDEX_LOGO)

    @allure.step("Прокрутка до веб-элемента")
    def scroll_to_element_with_web_element(self, element):
        """
        Прокрутить страницу до веб-элемента.

        Args:
            element: WebElement, до которого нужно прокрутить
        """
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element
        )

    @allure.step("Клик по веб-элементу через JavaScript")
    def click_element_with_web_element(self, element):
        """
        Кликнуть по веб-элементу через JavaScript.

        Args:
            element: WebElement, по которому нужно кликнуть
        """
        self.driver.execute_script("arguments[0].click();", element)
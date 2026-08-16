import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Page Object для главной страницы."""

    HEADER_HEIGHT = 80

    @allure.step("Клик по кнопке «Заказать» в шапке страницы")
    def click_order_button_header(self):
        """Клик по кнопке «Заказать» в шапке страницы."""
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Клик по кнопке «Заказать» в середине страницы")
    def click_order_button_middle(self):
        """Клик по кнопке «Заказать» в середине страницы."""
        self.scroll_to_pixels(self.HEADER_HEIGHT * 2)
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Клик по кнопке вопроса с индексом {index}")
    def click_question_button(self, index):
        items = self.wait_for_all_elements_visible(MainPageLocators.QUESTION_ITEMS)
        button = self.find_element_in_element(items[index], MainPageLocators.QUESTION_BUTTON)
        self.scroll_to_web_element(button)
        self.click_element(button)
        panel = self.find_element_in_element(items[index], MainPageLocators.QUESTION_PANEL)
        self.wait_for_web_element_visible(panel)

    @allure.step("Получение текста ответа на вопрос с индексом {index}")
    def get_question_answer_text(self, index):
        items = self.wait_for_all_elements_visible(MainPageLocators.QUESTION_ITEMS)
        panel = self.find_element_in_element(items[index], MainPageLocators.QUESTION_PANEL)
        self.wait_for_web_element_visible(panel)
        return panel.text

    @allure.step("Клик по логотипу «Самокат»")
    def click_scooter_logo(self):
        """Клик по логотипу «Самокат» — переход на главную страницу."""
        self.click_element_with_wait(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу «Яндекс»")
    def click_yandex_logo(self):
        """Клик по логотипу «Яндекс» — открытие Дзена в новой вкладке."""
        self.click_element_with_wait(MainPageLocators.YANDEX_LOGO)
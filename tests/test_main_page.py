import pytest

from pages.main_page import MainPage
from urls import Urls


QUESTION_DATA = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]


class TestMainPage:
    """Тесты для главной страницы."""

    @pytest.mark.parametrize(
        "question_index, expected_answer",
        QUESTION_DATA,
        ids=["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
    )
    def test_question_accordion(self, driver, question_index, expected_answer):
        """Проверка: при клике на вопрос открывается правильный текст ответа."""
        main_page = MainPage(driver)
        main_page.click_question_button(question_index)
        assert main_page.get_question_answer_text(question_index) == expected_answer

    def test_click_scooter_logo_returns_to_main_page(self, driver):
        """Проверка: клик по логотипу Самоката возвращает на главную страницу."""
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == Urls.BASE_URL

    def test_click_yandex_logo_opens_dzen(self, driver):
        """Проверка: клик по логотипу Яндекса открывает Дзен в новой вкладке."""
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        original_window = main_page.switch_to_new_window()
        main_page.wait_for_url_contains("dzen.ru")
        assert "dzen.ru" in main_page.get_current_url()
        main_page.switch_to_window(original_window)
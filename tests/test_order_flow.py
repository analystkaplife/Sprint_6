import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


ORDER_DATA = [
    (
        "Павел",
        "Иконописцев",
        "Москва, ул. Ленина, 1",
        "Сокольники",
        "+79991234567",
        2,
        "Позвонить за час до доставки",
    ),
    (
        "Анна",
        "Петрова",
        "Москва, Ленинградский проспект, 5",
        "Аэропорт",
        "+79876543210",
        4,
        "Оставить у двери",
    ),
]


class TestOrderFlow:
    """Тесты для сценария оформления заказа."""

    @pytest.mark.parametrize(
        "name, last_name, address, metro, phone, rental_days, comment",
        ORDER_DATA,
    )
    def test_order_from_header_button(
        self, driver, name, last_name, address, metro, phone, rental_days, comment
    ):
        """Полный позитивный сценарий: заказ через кнопку в шапке."""
        main_page = MainPage(driver)
        main_page.click_order_button_header()

        order_page = OrderPage(driver)
        order_page.fill_order_form(
            name=name,
            last_name=last_name,
            address=address,
            metro_station=metro,
            phone=phone,
            rental_days=rental_days,
            comment=comment,
        )
        order_page.confirm_order()

        assert order_page.is_order_successful()

    @pytest.mark.parametrize(
        "name, last_name, address, metro, phone, rental_days, comment",
        ORDER_DATA,
    )
    def test_order_from_middle_button(
        self, driver, name, last_name, address, metro, phone, rental_days, comment
    ):
        """Полный позитивный сценарий: заказ через кнопку в середине страницы."""
        main_page = MainPage(driver)
        main_page.click_order_button_middle()

        order_page = OrderPage(driver)
        order_page.fill_order_form(
            name=name,
            last_name=last_name,
            address=address,
            metro_station=metro,
            phone=phone,
            rental_days=rental_days,
            comment=comment,
        )
        order_page.confirm_order()

        assert order_page.is_order_successful()
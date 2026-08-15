import allure
import time

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from pages.order_modal_page import OrderModalPage


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
        """Инициализация страницы."""
        super().__init__(driver)
        self.modal = OrderModalPage(driver)

    @allure.step("Заполнение всей формы заказа")
    def fill_order_form(
        self,
        name: str,
        last_name: str,
        address: str,
        metro_station: str,
        phone: str,
        rental_days: int,
        comment: str,
    ):
        """
        Заполнить всю форму заказа: шаг 1 + шаг 2.

        Args:
            name: Имя арендатора.
            last_name: Фамилия арендатора.
            address: Адрес доставки.
            metro_station: Станция метро (для выбора из списка).
            phone: Телефон.
            rental_days: Срок аренды в днях (индекс опции).
            comment: Комментарий для курьера.
        """
        self._fill_renter_info(name, last_name, address, metro_station, phone)
        self._click_next_button()
        self._fill_rental_info(rental_days, comment)
        self._submit_order()

    @allure.step("Подтверждение заказа в модальном окне")
    def confirm_order(self):
        """Подтвердить заказ в модальном окне."""
        self.modal.click_confirm_button()

    @allure.step("Проверка успешного оформления заказа")
    def is_order_successful(self) -> bool:
        """
        Проверить, что заказ успешно оформлен.

        Returns:
            True, если сообщение «Заказ оформлен» отображается, иначе False.
        """
        return self.modal.is_success_message_visible()

    @allure.step("Заполнение полей «Про арендатора»")
    def _fill_renter_info(self, name, last_name, address, metro_station, phone):
        """Заполнение полей «Про арендатора» (приватный метод)."""
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)

        self._select_metro_station(metro_station)

        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Выбор станции метро: {metro_station}")
    def _select_metro_station(self, metro_station):
        """Выбор станции метро из выпадающего списка."""
        metro_input = self.driver.find_element(*OrderPageLocators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro_station)
        station_option = self.wait.until(
            self.EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_OPTION)
        )
        station_option.click()

    @allure.step("Клик по кнопке «Далее»")
    def _click_next_button(self):
        """Клик по кнопке «Далее»."""
        self.click_element_with_wait(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение полей «Про аренду»")
    def _fill_rental_info(self, rental_days, comment):
        """Заполнение полей «Про аренду» (приватный метод)."""
        self._select_delivery_date()
        self._select_rental_period(rental_days)
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Выбор даты доставки (сегодня)")
    def _select_delivery_date(self):
        """Выбор даты доставки (сегодня)."""
        date_input = self.find_element_with_wait(OrderPageLocators.DELIVERY_DATE_INPUT)
        date_input.click()
        
        today = self.wait.until(
            self.EC.element_to_be_clickable(OrderPageLocators.DATE_TODAY)
        )
        today.click()

    @allure.step("Выбор срока аренды: {rental_days} дней")
    def _select_rental_period(self, rental_days):
        """Выбор срока аренды из выпадающего списка."""
        dropdown = self.wait.until(
            self.EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        )
        dropdown.click()

        options = self.wait.until(
            self.EC.visibility_of_all_elements_located(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        )
        options[rental_days].click()

    @allure.step("Отправка заказа (клик по финальной кнопке «Заказать»)")
    def _submit_order(self):
        """Клик по финальной кнопке «Заказать» (приватный метод)."""
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_FINAL)
        time.sleep(0.3)
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON_FINAL)
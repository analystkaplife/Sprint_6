import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from pages.order_modal_page import OrderModalPage


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
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
        self._fill_renter_info(name, last_name, address, metro_station, phone)
        self._click_next_button()
        self._fill_rental_info(rental_days, comment)
        self._submit_order()

    @allure.step("Подтверждение заказа в модальном окне")
    def confirm_order(self):
        self.modal.click_confirm_button()

    @allure.step("Проверка успешного оформления заказа")
    def is_order_successful(self) -> bool:
        return self.modal.is_success_message_visible()

    @allure.step("Заполнение полей «Про арендатора»")
    def _fill_renter_info(self, name, last_name, address, metro_station, phone):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        self._select_metro_station(metro_station)
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Выбор станции метро: {metro_station}")
    def _select_metro_station(self, metro_station):
        metro_input = self.find_element_with_wait(OrderPageLocators.METRO_STATION_INPUT)
        self.click_web_element(metro_input)
        self.send_keys_to_web_element(metro_input, metro_station)
        station_option = self.wait_for_element_clickable(OrderPageLocators.METRO_STATION_OPTION)
        self.click_web_element(station_option)

    @allure.step("Клик по кнопке «Далее»")
    def _click_next_button(self):
        self.click_element_with_wait(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение полей «Про аренду»")
    def _fill_rental_info(self, rental_days, comment):
        self._select_delivery_date()
        self._select_rental_period(rental_days)
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Выбор даты доставки (сегодня)")
    def _select_delivery_date(self):
        date_input = self.find_element_with_wait(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.click_web_element(date_input)
        today = self.wait_for_element_clickable( OrderPageLocators.DATE_TODAY)
        self.click_web_element(today)

    @allure.step("Выбор срока аренды: {rental_days} дней")
    def _select_rental_period(self, rental_days):
        dropdown = self.wait_for_element_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_web_element(dropdown)
        options = self.wait_for_all_elements_visible(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        self.click_web_element(options[rental_days])

    @allure.step("Отправка заказа (клик по финальной кнопке «Заказать»)")
    def _submit_order(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_FINAL)
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON_FINAL)
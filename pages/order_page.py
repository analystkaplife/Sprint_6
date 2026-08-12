from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators
from pages.order_modal_page import OrderModalPage


class OrderPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
        """Инициализация страницы."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.modal = OrderModalPage(driver)

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

    def confirm_order(self):
        """Подтвердить заказ в модальном окне."""
        self.modal.click_confirm_button()

    def is_order_successful(self) -> bool:
        """
        Проверить, что заказ успешно оформлен.

        Returns:
            True, если сообщение «Заказ оформлен» отображается, иначе False.
        """
        return self.modal.is_success_message_visible()

    def _fill_renter_info(self, name, last_name, address, metro_station, phone):
        """Заполнение полей «Про арендатора» (приватный метод)."""
        self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)
        ).send_keys(name)
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

        # Работа с выпадающим списком станций метро
        metro_input = self.driver.find_element(*OrderPageLocators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro_station)
        station_option = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_OPTION)
        )
        station_option.click()

        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)

    def _click_next_button(self):
        """Клик по кнопке «Далее»."""
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)).click()

    def _fill_rental_info(self, rental_days, comment):
        """Заполнение полей «Про аренду» (приватный метод)."""
        # Заполняем дату доставки
        date_input = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.DELIVERY_DATE_INPUT)
        )
        date_input.click()
        # Выбираем сегодняшний день в календаре
        today = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.DATE_TODAY)
        )
        today.click()

        # Выбираем срок аренды
        dropdown = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        )
        dropdown.click()

        # Выбираем нужный срок
        options = self.wait.until(
            EC.visibility_of_all_elements_located(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        )
        options[rental_days].click()

        # Комментарий
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    def _submit_order(self):
        """Клик по финальной кнопке «Заказать» (приватный метод)."""
        order_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_FINAL)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", order_button
        )
        order_button.click()
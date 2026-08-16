import allure

from pages.base_page import BasePage
from locators.order_modal_page_locators import OrderModalPageLocators


class OrderModalPage(BasePage):
    """Page Object для модального окна подтверждения заказа. """

    @allure.step("Клик по кнопке «Да» для подтверждения заказа")
    def click_confirm_button(self):
        """Клик по кнопке «Да» для подтверждения заказа."""
        confirm_button = self.wait_for_element_clickable(OrderModalPageLocators.CONFIRM_BUTTON)
        self.click_web_element(confirm_button)

    @allure.step("Проверка отображения сообщения об успешном оформлении заказа")
    def is_success_message_visible(self) -> bool:
        try:
            self.wait_for_element_visible(OrderModalPageLocators.SUCCESS_MESSAGE)
            return True
        except Exception:
            return False
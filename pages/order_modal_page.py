import allure

from pages.base_page import BasePage
from locators.order_modal_page_locators import OrderModalPageLocators


class OrderModalPage(BasePage):
    """Page Object для модального окна подтверждения заказа."""

    @allure.step("Клик по кнопке «Да» для подтверждения заказа")
    def click_confirm_button(self):
        """Клик по кнопке «Да» для подтверждения заказа."""
        self.click_element_with_wait(OrderModalPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверка отображения сообщения об успешном оформлении заказа")
    def is_success_message_visible(self) -> bool:
        """
        Проверить, что сообщение об успехе отображается.

        Returns:
            True, если сообщение «Заказ оформлен» видно, иначе False.
        """
        try:
            self.find_element_with_wait(OrderModalPageLocators.SUCCESS_MESSAGE)
            return True
        except Exception:
            return False
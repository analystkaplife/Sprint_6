from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_modal_page_locators import OrderModalPageLocators


class OrderModalPage:
    """Page Object для модального окна подтверждения заказа."""

    def __init__(self, driver):
        """Инициализация модального окна."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_confirm_button(self):
        """Клик по кнопке «Да» для подтверждения заказа."""
        button = self.wait.until(
            EC.element_to_be_clickable(OrderModalPageLocators.CONFIRM_BUTTON)
        )
        button.click()

    def is_success_message_visible(self) -> bool:
        """
        Проверить, что сообщение об успехе отображается.

        Returns:
            True, если сообщение «Заказ оформлен» видно, иначе False.
        """
        try:
            # Ждём появления сообщения "Заказ оформлен"
            message = self.wait.until(
                EC.visibility_of_element_located(OrderModalPageLocators.SUCCESS_MESSAGE)
            )
            return True
        except Exception:
            return False
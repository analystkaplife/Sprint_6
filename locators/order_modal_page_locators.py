from selenium.webdriver.common.by import By


class OrderModalPageLocators:
    """Локаторы для модального окна подтверждения заказа."""

    # Кнопка "Да" в модальном окне "Хотите оформить заказ?"
    CONFIRM_BUTTON = By.XPATH, ".//button[text()='Да']"

    # Сообщение об успехе (появляется ПОСЛЕ нажатия "Да")
    SUCCESS_MESSAGE = By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]"
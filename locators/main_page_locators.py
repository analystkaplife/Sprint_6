from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы. """

    # Кнопки «Заказать»
    ORDER_BUTTON_HEADER = By.XPATH, ".//button[contains(@class, 'Button_Button') and text()='Заказать']"
    ORDER_BUTTON_MIDDLE = By.XPATH, ".//button[contains(@class, 'Button_UltraBig') and text()='Заказать']"

    # Логотипы
    SCOOTER_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"
    YANDEX_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"

    # Вопросы о важном (аккордеон)
    QUESTION_ITEMS = By.XPATH, ".//div[contains(@class, 'accordion__item')]"
    QUESTION_BUTTON = By.XPATH, ".//div[contains(@class, 'accordion__button')]"
    QUESTION_PANEL = By.XPATH, ".//div[contains(@class, 'accordion__panel')]"
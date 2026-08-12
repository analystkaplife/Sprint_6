from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы оформления заказа."""

    # Шаг 1: «Про арендатора»
    NAME_INPUT = By.XPATH, ".//input[@placeholder='* Имя']"
    LAST_NAME_INPUT = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_INPUT = By.XPATH, ".//input[@placeholder='* Станция метро']"
    METRO_STATION_OPTION = By.XPATH, ".//div[contains(@class, 'select-search__select')]//button"
    PHONE_INPUT = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, ".//button[text()='Далее']"

    # Шаг 2: «Про аренду»
    DELIVERY_DATE_INPUT = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    DATE_TODAY = By.XPATH, ".//div[contains(@class, 'react-datepicker__day--today')]"
    
    RENTAL_PERIOD_DROPDOWN = By.XPATH, ".//div[contains(@class, 'Dropdown-control')]"
    RENTAL_PERIOD_OPTIONS = By.XPATH, ".//div[contains(@class, 'Dropdown-option')]"
    
    COMMENT_INPUT = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON_FINAL = By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']"
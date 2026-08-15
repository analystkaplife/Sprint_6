import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.EC = EC

    @allure.step("Поиск элемента с ожиданием его видимости")
    def find_element_with_wait(self, locator):
        """
        Найти элемент с ожиданием его видимости.
        
        Args:
            locator: Кортеж (By, selector)
        
        Returns:
            WebElement: Найденный элемент
        """
        self.wait.until(self.EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу с ожиданием его кликабельности")
    def click_element_with_wait(self, locator):
        """
        Кликнуть по элементу с ожиданием его кликабельности.
        
        Args:
            locator: Кортеж (By, selector)
        """
        self.wait.until(self.EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста в элемент")
    def send_keys_to_element(self, locator, text):
        """
        Ввести текст в элемент с ожиданием его видимости.
        
        Args:
            locator: Кортеж (By, selector)
            text: Текст для ввода
        """
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Прокрутка страницы до элемента")
    def scroll_to_element(self, locator):
        """
        Прокрутить страницу до элемента.
        
        Args:
            locator: Кортеж (By, selector)
        
        Returns:
            WebElement: Элемент, до которого прокрутили
        """
        element = self.find_element_with_wait(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element
        )
        return element

    @allure.step("Прокрутка страницы на указанное количество пикселей")
    def scroll_to_pixels(self, pixels: int):
        """
        Прокрутить страницу на указанное количество пикселей.
        
        Args:
            pixels: Количество пикселей для прокрутки
        """
        self.driver.execute_script(f"window.scrollTo(0, {pixels});")

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self) -> str:
        """Получить текущий URL страницы."""
        return self.driver.current_url

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_window(self):
        """
        Переключиться на новую вкладку браузера.

        Returns:
            Handle исходной вкладки.
        """
        self.wait.until(self.EC.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        return original_window

    @allure.step("Переключение на вкладку по handle")
    def switch_to_window(self, window_handle):
        """Переключиться на вкладку с указанным handle."""
        self.driver.switch_to.window(window_handle)

    @allure.step("Ожидание, пока URL не будет содержать указанную подстроку")
    def wait_for_url_contains(self, expected_url_part: str):
        """
        Дождаться, пока URL текущей вкладки не будет содержать указанную подстроку.

        Args:
            expected_url_part: Часть ожидаемого URL (например, "dzen.ru").
        """
        self.wait.until(
            lambda driver: expected_url_part in driver.current_url
        )
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.EC = EC

    # ============ МЕТОДЫ ОЖИДАНИЯ ============

    @allure.step("Поиск элемента с ожиданием его видимости")
    def find_element_with_wait(self, locator):
        """Найти элемент с ожиданием его видимости."""
        self.wait.until(self.EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Поиск элемента внутри другого элемента")
    def find_element_in_element(self, parent_element, locator):
        """
        Найти элемент внутри родительского элемента.
        
        Args:
            parent_element: WebElement, внутри которого ищем
            locator: Кортеж (By, selector)
        
        Returns:
            WebElement: Найденный элемент
        """
        return parent_element.find_element(*locator)

    @allure.step("Ожидание видимости элемента по локатору")
    def wait_for_element_visible(self, locator):
        """Ожидать видимость элемента по локатору."""
        return self.wait.until(self.EC.visibility_of_element_located(locator))

    @allure.step("Ожидание видимости веб-элемента")
    def wait_for_web_element_visible(self, element):
        """Ожидать, пока переданный веб-элемент станет видимым."""
        self.wait.until(self.EC.visibility_of(element))
        return element

    @allure.step("Ожидание кликабельности элемента и его получение")
    def wait_for_element_clickable(self, locator):
        """Ожидать, пока элемент станет кликабельным, и вернуть его."""
        return self.wait.until(self.EC.element_to_be_clickable(locator))

    @allure.step("Ожидание видимости всех элементов")
    def wait_for_all_elements_visible(self, locator):
        """Ожидать, пока все элементы станут видимыми."""
        return self.wait.until(
            self.EC.visibility_of_all_elements_located(locator)
        )

    # ============ МЕТОДЫ КЛИКА ============

    @allure.step("Клик по элементу с ожиданием его кликабельности")
    def click_element_with_wait(self, locator):
        """Кликнуть по элементу с ожиданием его кликабельности."""
        self.wait.until(self.EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Клик по веб-элементу")
    def click_web_element(self, element):
        """Кликнуть по переданному веб-элементу."""
        self.wait.until(self.EC.element_to_be_clickable(element))
        element.click()

    @allure.step("Клик по веб-элементу")
    def click_element(self, element):
        """Кликнуть по переданному веб-элементу через JavaScript."""
        self.wait.until(self.EC.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click();", element) 

    # ============ МЕТОДЫ ВВОДА ТЕКСТА ============

    @allure.step("Ввод текста в элемент")
    def send_keys_to_element(self, locator, text):
        """Ввести текст в элемент с ожиданием его видимости."""
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Ввод текста в веб-элемент")
    def send_keys_to_web_element(self, element, text):
        """Ввести текст в переданный веб-элемент."""
        element.clear()
        element.send_keys(text)

    # ============ МЕТОДЫ ПРОКРУТКИ ============

    @allure.step("Прокрутка страницы до элемента")
    def scroll_to_element(self, locator):
        """Прокрутить страницу до элемента."""
        element = self.find_element_with_wait(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element
        )
        return element

    @allure.step("Прокрутка до веб-элемента")
    def scroll_to_web_element(self, element):
        """Прокрутить страницу до веб-элемента."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element
        )

    @allure.step("Прокрутка страницы на указанное количество пикселей")
    def scroll_to_pixels(self, pixels: int):
        """Прокрутить страницу на указанное количество пикселей."""
        self.driver.execute_script(f"window.scrollTo(0, {pixels});")

    # ============ МЕТОДЫ ДЛЯ РАБОТЫ С URL ============

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self) -> str:
        """Получить текущий URL страницы."""
        return self.driver.current_url

    @allure.step("Ожидание, пока URL не будет содержать указанную подстроку")
    def wait_for_url_contains(self, expected_url_part: str):
        """Дождаться, пока URL текущей вкладки не будет содержать указанную подстроку."""
        self.wait.until(
            lambda driver: expected_url_part in driver.current_url
        )

    # ============ МЕТОДЫ ДЛЯ РАБОТЫ С ОКНАМИ ============

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_window(self):
        """Переключиться на новую вкладку браузера."""
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
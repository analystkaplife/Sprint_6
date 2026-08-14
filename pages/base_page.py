from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.EC = EC

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

    def click_element_with_wait(self, locator):
        """
        Кликнуть по элементу с ожиданием его кликабельности.
        
        Args:
            locator: Кортеж (By, selector)
        """
        self.wait.until(self.EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

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
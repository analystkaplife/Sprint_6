from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://qa-scooter.praktikum-services.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
time.sleep(2)

# Шаг 1: клик по кнопке "Заказать" в шапке
print("Кликаем по кнопке Заказать в шапке...")
order_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[contains(@class, 'Button_Button') and text()='Заказать']")))
order_button.click()
time.sleep(2)

# Шаг 2: заполняем форму
print("Заполняем форму...")
name_input = wait.until(EC.visibility_of_element_located((By.XPATH, ".//input[@placeholder='* Имя']")))
name_input.send_keys("Павел")
driver.find_element(By.XPATH, ".//input[@placeholder='* Фамилия']").send_keys("Иконописцев")
driver.find_element(By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']").send_keys("Москва, ул. Ленина, 1")

# Метро
metro_input = driver.find_element(By.XPATH, ".//input[@placeholder='* Станция метро']")
metro_input.click()
metro_input.send_keys("Сокольники")
station = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[contains(@class, 'select-search__select')]//button")))
station.click()
time.sleep(1)

driver.find_element(By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys("+79991234567")

# Кнопка "Далее"
print("Нажимаем Далее...")
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Далее']")))
next_button.click()
time.sleep(2)

# Шаг 3: заполняем дату
print("Заполняем дату...")
date_input = wait.until(EC.visibility_of_element_located((By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")))
date_input.click()
time.sleep(1)

# Пробуем выбрать сегодняшний день
try:
    today = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[contains(@class, 'react-datepicker__day--today')]")))
    today.click()
    print("Выбрали сегодняшний день")
except Exception as e:
    print(f"Не смогли выбрать день: {e}")
    # Альтернатива: вводим дату вручную
    date_input.send_keys("31.12.2025")
    date_input.send_keys(Keys.ENTER)
    print("Ввели дату вручную")

time.sleep(1)

# Шаг 4: выбираем срок аренды
print("Выбираем срок аренды...")
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[contains(@class, 'Dropdown-control')]")))
dropdown.click()
time.sleep(1)

# Ищем опции
options = driver.find_elements(By.XPATH, ".//div[contains(@class, 'Dropdown-option')]")
print(f"Найдено опций: {len(options)}")
for i, opt in enumerate(options):
    print(f"Опция {i}: text='{opt.text}'")

# Выбираем вторую (индекс 2 = "двое суток")
if len(options) > 2:
    options[2].click()
    print("Выбрали 2 суток")
else:
    print("Опций недостаточно!")

time.sleep(1)

# Шаг 5: комментарий
print("Заполняем комментарий...")
comment_input = driver.find_element(By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
comment_input.send_keys("Позвонить за час до доставки")

# Шаг 6: кнопка "Заказать"
print("Нажимаем кнопку Заказать...")
order_final = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']")))
order_final.click()
time.sleep(2)

# Шаг 7: проверяем модальное окно
print("Проверяем модальное окно...")
try:
    modal = wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[contains(@class, 'Order_Modal')]")))
    print(f"Модальное окно найдено: {modal.text[:100]}")
    
    # Нажимаем "Да"
    confirm = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Да']")))
    confirm.click()
    time.sleep(2)
    
    # Проверяем сообщение
    success = wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")))
    print(f"Сообщение: {success.text}")
except Exception as e:
    print(f"Ошибка: {e}")
    # Скриншот
    driver.save_screenshot("debug_screenshot.png")
    print("Скриншот сохранён: debug_screenshot.png")

driver.quit()
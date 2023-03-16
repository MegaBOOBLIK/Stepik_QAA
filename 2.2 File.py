from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[contains(@name,'firstname')]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@name,'lastname')]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[contains(@name,'email')]")
    input3.send_keys("ivan@petrov.ru")

    element = browser.find_element(By.XPATH, "//input[contains(@id,'file')]")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[contains(@type,'submit')]")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

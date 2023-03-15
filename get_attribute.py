from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    findx = browser.find_element(By.XPATH, "//img")

    x = findx.get_attribute("valuex")
    print(x)

    # assert people_checked is not None, "People radio is not selected by default"
    # x_element = browser.find_element(By.CSS_SELECTOR, "element.style")
    # x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    # x = x_element.text
    y = calc(x)
    print(y)

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)


    # input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'last name')]")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'email')]")
    # input3.send_keys("ivan@petrov.ru")

    option1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)
    #
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
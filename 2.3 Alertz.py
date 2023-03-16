from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)

    # option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    # option1.click()
    #
    # option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    # option2.click()

    # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button2.click()

    time.sleep(1)

    print(browser.switch_to.alert.text)

    alert2 = browser.switch_to.alert
    alert2.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


# button_element = driver.find_element_by_link_text("Start Free Testing")
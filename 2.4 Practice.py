from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.XPATH, "//button[@id='book']")
    button.click()

    # text_to_be_present_in_element_value

    # win2 = browser.window_handles[1]
    # browser.switch_to.window(win2)
    # alert = browser.switch_to.alert
    # alert.accept()

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

    print(browser.switch_to.alert.text)

    alert2 = browser.switch_to.alert
    alert2.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


# button_element = driver.find_element_by_link_text("Start Free Testing")
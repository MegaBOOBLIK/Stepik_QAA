from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link1 = "https://suninjuly.github.io/selects1.html"
    link2 = "https://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()


    browser.get(link2)
    #browser.execute_script("alert('Robots at work');")
    #time.sleep(3)

    x1 = browser.find_element(By.XPATH, "//span[@id='num1']")
    x2 = browser.find_element(By.XPATH, "//span[@id='num2']")

    x = int(x1.text) + int(x2.text)

    print(x)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

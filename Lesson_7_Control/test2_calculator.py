from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options)


driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
sleep(1)

delay = driver.find_element(By.CSS_SELECTOR, "#delay")
delay.clear()
delay.send_keys("45")

driver.find_element(
    By.CSS_SELECTOR, "span.clear.btn.btn-outline-danger").click()

digits = driver.find_elements(By.CSS_SELECTOR, "span.btn.btn-outline-primary")
operators = driver.find_elements(
    By.CSS_SELECTOR, "span.operator.btn.btn-outline-success")

seven = digits[0]
seven.click()

plus = operators[0]
plus.click()

eight = digits[1]
eight.click()

driver.find_element(By.CSS_SELECTOR, "span.btn.btn-outline-warning").click()

try:
    sleep(44)
    result = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    # print(result)
    assert result == "15"

except AssertionError:
    sleep(1)
    result = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    # print(result)
    assert result == "15"


sleep(2)
driver.quit

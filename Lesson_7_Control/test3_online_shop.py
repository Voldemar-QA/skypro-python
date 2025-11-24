from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options)


driver.get("https://www.saucedemo.com/")
sleep(1)

username = driver.find_element(By.CSS_SELECTOR, "#user-name")
username.send_keys("standard_user")
sleep(1)

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#login-button").click()
sleep(1)

driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
sleep(1)

driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
sleep(1)

driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
sleep(1)

driver.find_element(
    By.CSS_SELECTOR, "a.shopping_cart_link").click()
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#checkout").click()
sleep(1)

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("John")
sleep(1)

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Doe")
sleep(1)

zip_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
zip_code.send_keys("135813")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#continue").click()
sleep(1)

total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
print(total)
amount = total.split(": ")[1]
print(amount)
assert amount == "$58.29"

sleep(2)
driver.quit

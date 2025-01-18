from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Задание 3. Клик по кнопке
# Chrome:

c_driver = webdriver.Chrome(service=ChromeService
                            (ChromeDriverManager().install())
                            )

# c_driver.maximize_window()

c_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_element = "button[onclick='addElement()']"
button = c_driver.find_element(By.CSS_SELECTOR, add_element)
for x in range(5):
    button.click()
    sleep(1)

sleep(3)

add_element = "button.added-manually"

del_buttons = c_driver.find_elements(By.CSS_SELECTOR, add_element)

print(
    "Число добавленных кнопок 'Delete' на странице в браузере Chrome: ",
    len(del_buttons)
    )

c_driver.quit()


# Firefox:

f_driver = webdriver.Firefox(service=FirefoxService
                             (GeckoDriverManager().install())
                             )

f_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_element = "button[onclick='addElement()']"
button = f_driver.find_element(By.CSS_SELECTOR, add_element)
for x in range(5):
    button.click()
    sleep(1)

sleep(3)
add_element = "button.added-manually"

del_buttons = f_driver.find_elements(By.CSS_SELECTOR, add_element)

print(
    "Число добавленных кнопок 'Delete' на странице в браузере Firefox: ",
    len(del_buttons)
    )

f_driver.quit()

print("Задание 1 выполнено.")


# Задание 4. Клик по кнопке без ID
# Chrome:

for x in range(3):
    c_driver = webdriver.Chrome(service=ChromeService
                                (ChromeDriverManager().install())
                                )
    c_driver.get("http://uitestingplayground.com/dynamicid")
    locator = "button.btn.btn-primary"
    button = c_driver.find_element(By.CSS_SELECTOR, locator)
    button.click()
    sleep(1)
    print("Chrome click")
    c_driver.quit()


# Firefox:

for x in range(3):
    f_driver = webdriver.Firefox(service=FirefoxService
                                 (GeckoDriverManager().install())
                                 )
    f_driver.get("http://uitestingplayground.com/dynamicid")
    locator = "button.btn.btn-primary"
    button = f_driver.find_element(By.CSS_SELECTOR, locator)
    button.click()
    sleep(1)
    print("Firefox click")
    f_driver.quit()

print("Задание 4 выполнено.")


# Задание 5. Клик по кнопке с CSS-классом
# Chrome:

for x in range(3):
    c_driver = webdriver.Chrome(service=ChromeService
                                (ChromeDriverManager().install())
                                )
    c_driver.get("http://uitestingplayground.com/classattr")
    locator = "button.btn-primary"
    button = c_driver.find_element(By.CSS_SELECTOR, locator)
    button.click()
    sleep(3)
    print("Chrome click")
    c_driver.quit()


# Firefox:

for x in range(3):
    f_driver = webdriver.Firefox(service=FirefoxService
                                 (GeckoDriverManager().install())
                                 )
    f_driver.get("http://uitestingplayground.com/classattr")
    locator = "button.btn-primary"
    button = f_driver.find_element(By.CSS_SELECTOR, locator)
    button.click()
    sleep(3)
    print("Firefox click")
    f_driver.quit()

print("Задание 5 выполнено.")


# Задание 6. Модальное окно
# Chrome:

c_driver = webdriver.Chrome(service=ChromeService
                            (ChromeDriverManager().install())
                            )

c_driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)
locator = "#modal .modal .modal-footer p"
button = c_driver.find_element(By.CSS_SELECTOR, locator)
button.click()
print("Chrome click")
sleep(3)
c_driver.quit()


# Firefox:

f_driver = webdriver.Firefox(service=FirefoxService
                             (GeckoDriverManager().install())
                             )

f_driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)
locator = "#modal .modal .modal-footer p"
button = f_driver.find_element(By.CSS_SELECTOR, locator)
button.click()
print("Firefox click")
sleep(3)
f_driver.quit()

print("Задание 6 выполнено.")


# Задание 7. Поле ввода
# Chrome:

c_driver = webdriver.Chrome(service=ChromeService
                            (ChromeDriverManager().install())
                            )

c_driver.get("http://the-internet.herokuapp.com/inputs")
field = c_driver.find_element(By.CSS_SELECTOR, "input")
sleep(2)
field.send_keys("1000")
sleep(2)
field.clear()
sleep(2)
field.send_keys("999")
sleep(2)
c_driver.quit()


# Firefox:

f_driver = webdriver.Firefox(service=FirefoxService
                             (GeckoDriverManager().install())
                             )

f_driver.get("http://the-internet.herokuapp.com/inputs")
field = f_driver.find_element(By.CSS_SELECTOR, "input")
sleep(2)
field.send_keys("1000")
sleep(2)
field.clear()
sleep(2)
field.send_keys("999")
sleep(2)
f_driver.quit()

print("Задание 7 выполнено.")


# Задание 8. Форма авторизации
# Chrome:

c_driver = webdriver.Chrome(service=ChromeService
                            (ChromeDriverManager().install())
                            )

c_driver.get("http://the-internet.herokuapp.com/login")
username = c_driver.find_element(By.CSS_SELECTOR, "#username")
sleep(1)
username.send_keys("tomsmith")
password = c_driver.find_element(By.CSS_SELECTOR, "#password")
sleep(1)
password.send_keys("SuperSecretPassword!")
sleep(1)
login_btn = c_driver.find_element(By.CSS_SELECTOR, "button.radius")
login_btn.click()
sleep(3)
c_driver.quit()


# Firefox:

f_driver = webdriver.Firefox(service=FirefoxService
                             (GeckoDriverManager().install())
                             )

f_driver.get("http://the-internet.herokuapp.com/login")
username = f_driver.find_element(By.CSS_SELECTOR, "#username")
sleep(1)
username.send_keys("tomsmith")
password = f_driver.find_element(By.CSS_SELECTOR, "#password")
sleep(1)
password.send_keys("SuperSecretPassword!")
sleep(1)
login_btn = f_driver.find_element(By.CSS_SELECTOR, "button.radius")
login_btn.click()
sleep(3)
f_driver.quit()


print("Задание 8 выполнено.")

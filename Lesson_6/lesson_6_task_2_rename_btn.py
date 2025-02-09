from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep


chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

chrome.get("http://uitestingplayground.com/textinput")

field = chrome.find_element(By.CSS_SELECTOR, "#newButtonName")

field.send_keys("Skypro")

button = WebDriverWait(chrome, 5).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#updatingButton"))
    )

# button = chrome.find_element(By.CSS_SELECTOR, "#updatingButton")

button.click()

text_button = chrome.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(text_button)

# sleep(5)

chrome.quit()

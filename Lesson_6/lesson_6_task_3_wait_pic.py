from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

waiter = WebDriverWait(chrome, 33)

chrome.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "p#text.lead"), "Done!")
    )

pics = chrome.find_elements(By.CSS_SELECTOR, "img")

# print(len(pics))

pic = pics[3]

source = pic.get_attribute("src")

print("Значение атрибута src у 3-й картинки:", source)

chrome.quit()

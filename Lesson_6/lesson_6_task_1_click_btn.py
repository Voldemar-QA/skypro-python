from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

chrome.implicitly_wait(16)

chrome.get("http://uitestingplayground.com/ajax")

chrome.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = chrome.find_element(By.CSS_SELECTOR, "#content"
                              )
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

chrome.quit()

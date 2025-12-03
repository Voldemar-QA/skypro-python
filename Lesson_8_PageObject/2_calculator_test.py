from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.calc_page import CalcPage

delay = "45"

def test_calculator_delay():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=options)

    calc_page = CalcPage(browser)
    calc_page.set_delay(delay)
    calc_page.clear_input()

    all_digits = calc_page.all_digits()
    seven = all_digits[0]
    seven.click()

    all_operators = calc_page.all_operators()
    plus = all_operators[0]
    plus.click()

    eight = all_digits[1]
    eight.click()

    calc_page.equal_to()
    
    try:
        sleep(44)
        number = calc_page.result()
        assert number == "15"

    except AssertionError:
        sleep(1)
        number = calc_page.result()
        assert number == "15"


    sleep(2)
    browser.quit

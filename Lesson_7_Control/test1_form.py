from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(options=options)


browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
sleep(1)

first_name = browser.find_element(By.CSS_SELECTOR, "[name = first-name]")
first_name.send_keys("Иван")
sleep(1)

last_name = browser.find_element(By.CSS_SELECTOR, "[name = last-name]")
last_name.send_keys("Петров")
sleep(1)

address = browser.find_element(By.CSS_SELECTOR, "[name = address]")
address.send_keys("Ленина, 55-3")
sleep(1)

city = browser.find_element(By.CSS_SELECTOR, "[name = city]")
city.send_keys("Москва")
sleep(1)

country = browser.find_element(By.CSS_SELECTOR, "[name = country]")
country.send_keys("Россия")
sleep(1)

email = browser.find_element(By.CSS_SELECTOR, "[name = e-mail]")
email.send_keys("test@skypro.com")
sleep(1)

phone = browser.find_element(By.CSS_SELECTOR, "[name = phone]")
phone.send_keys("+7985899998787")
sleep(1)

job = browser.find_element(By.CSS_SELECTOR, "[name = job-position]")
job.send_keys("QA")
sleep(1)

company = browser.find_element(By.CSS_SELECTOR, "[name = company]")
company.send_keys("SkyPro")
sleep(1)

submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn-outline-primary")
submit_btn.click()


def test_zip_alert():
    zip_alert = browser.find_element(
        By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert zip_alert == "alert py-2 alert-danger"


def test_first_name_alert():
    first_name_alert = browser.find_element(
        By.CSS_SELECTOR, "#first-name").get_attribute("class")
    assert first_name_alert == "alert py-2 alert-success"


def test_last_name_alert():
    last_name_alert = browser.find_element(
        By.CSS_SELECTOR, "#last-name").get_attribute("class")
    assert last_name_alert == "alert py-2 alert-success"


def test_address_alert():
    address_alert = browser.find_element(
        By.CSS_SELECTOR, "#address").get_attribute("class")
    assert address_alert == "alert py-2 alert-success"


def test_city_alert():
    city_alert = browser.find_element(
        By.CSS_SELECTOR, "#city").get_attribute("class")
    assert city_alert == "alert py-2 alert-success"


def test_country_alert():
    country_alert = browser.find_element(
        By.CSS_SELECTOR, "#country").get_attribute("class")
    assert country_alert == "alert py-2 alert-success"


def test_email_alert():
    email_alert = browser.find_element(
        By.CSS_SELECTOR, "#e-mail").get_attribute("class")
    assert email_alert == "alert py-2 alert-success"


def test_phone_alert():
    phone_alert = browser.find_element(
        By.CSS_SELECTOR, "#phone").get_attribute("class")
    assert phone_alert == "alert py-2 alert-success"


def test_job_alert():
    job_alert = browser.find_element(
        By.CSS_SELECTOR, "#job-position").get_attribute("class")
    assert job_alert == "alert py-2 alert-success"


def test_company_alert():
    company_alert = browser.find_element(
        By.CSS_SELECTOR, "#company").get_attribute("class")
    assert company_alert == "alert py-2 alert-success"


sleep(2)
browser.quit

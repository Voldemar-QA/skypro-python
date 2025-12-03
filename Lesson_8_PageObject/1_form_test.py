from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.form_page import FormPage

var_first_name = "Иван"
var_last_name = "Петров"
var_address = "Ленина, 55-3"
var_city = "Москва"
var_country = "Россия"
var_email = "test@skypro.com"
var_phone = "+7985899998787"
var_job = "QA"
var_company = "SkyPro"
red_alert = "alert py-2 alert-danger"
green_ok = "alert py-2 alert-success"


def test_form_fields():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=options)

    form_page = FormPage(browser)
    form_page.first_name(var_first_name)
    form_page.last_name(var_last_name)
    form_page.address(var_address)
    form_page.city(var_city)
    form_page.country(var_country)
    form_page.email(var_email)
    form_page.phone(var_phone)
    form_page.job(var_job)
    form_page.company(var_company)
    form_page.submit_btn()

    zip_alert = form_page.zip_info()
    assert zip_alert == red_alert

    fst_name_alert = form_page.fst_name_info()
    assert fst_name_alert == green_ok
    
    lst_name_alert = form_page.lst_name_info()
    assert lst_name_alert == green_ok
    
    address_alert = form_page.address_info()
    assert address_alert == green_ok

    city_alert = form_page.city_info()
    assert city_alert == green_ok

    country_alert = form_page.country_info()
    assert country_alert == green_ok

    email_alert = form_page.email_info()
    assert email_alert == green_ok

    phone_alert = form_page.phone_info()
    assert phone_alert == green_ok

    job_alert = form_page.job_info()
    assert job_alert == green_ok

    company_alert = form_page.company_info()
    assert company_alert == green_ok


    sleep(2)
    browser.quit

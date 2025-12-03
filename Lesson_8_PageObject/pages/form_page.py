from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def first_name(self, var_first_name):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = first-name]").send_keys(var_first_name)

    def last_name(self, var_last_name):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = last-name]").send_keys(var_last_name)

    def address(self, var_address):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = address]").send_keys(var_address)

    def city(self, var_city):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = city]").send_keys(var_city)
    
    def country(self, var_country):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = country]").send_keys(var_country)
    
    def email(self, var_email):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = e-mail]").send_keys(var_email)
    
    def phone(self, var_phone):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = phone]").send_keys(var_phone)
    
    def job(self, var_job):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = job-position]").send_keys(var_job)
    
    def company(self, var_company):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name = company]").send_keys(var_company)

    def submit_btn(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button.btn-outline-primary").click()

    def zip_info(self):
        var_zip_info = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return (var_zip_info)
    
    def fst_name_info(self):
        var_fst_name_info = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").get_attribute("class")
        return (var_fst_name_info)
    
    def lst_name_info(self):
        var_lst_name_info = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").get_attribute("class")
        return (var_lst_name_info)

    def address_info(self):
        var_address_info = self.driver.find_element(
            By.CSS_SELECTOR, "#address").get_attribute("class")
        return (var_address_info)
    
    def city_info(self):
        var_city_info = self.driver.find_element(
            By.CSS_SELECTOR, "#city").get_attribute("class")
        return (var_city_info)
    
    def country_info(self):
        var_country_info = self.driver.find_element(
            By.CSS_SELECTOR, "#country").get_attribute("class")
        return (var_country_info)
    
    def email_info(self):
        var_email_info = self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail").get_attribute("class")
        return (var_email_info)
    
    def phone_info(self):
        var_phone_info = self.driver.find_element(
            By.CSS_SELECTOR, "#phone").get_attribute("class")
        return (var_phone_info)
    
    def job_info(self):
        var_job_info = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position").get_attribute("class")
        return (var_job_info)
    
    def company_info(self):
        var_company_info = self.driver.find_element(
            By.CSS_SELECTOR, "#company").get_attribute("class")
        return (var_company_info)

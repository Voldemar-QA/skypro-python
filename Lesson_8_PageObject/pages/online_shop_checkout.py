from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def first_name(self, var_first_name):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(var_first_name)

    def last_name(self, var_last_name):
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(var_last_name)

    def zip(self, var_zip):
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(var_zip)

    def summary(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()

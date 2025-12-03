from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def username(self, user_name):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(user_name)

    def password(self, parol):
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(parol)

    def login(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()

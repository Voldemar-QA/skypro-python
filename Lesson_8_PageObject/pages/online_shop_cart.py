from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def checkout_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

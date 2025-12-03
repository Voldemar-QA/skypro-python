from selenium.webdriver.common.by import By


class CalcPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def set_delay(self, delay):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(delay)

    def clear_input(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "span.clear.btn.btn-outline-danger").click()

    def all_digits(self):
        digits = self.driver.find_elements(
            By.CSS_SELECTOR, "span.btn.btn-outline-primary")
        return (digits)
    
    def all_operators(self):
        operators = self.driver.find_elements(
            By.CSS_SELECTOR, "span.operator.btn.btn-outline-success")
        return (operators)

    def equal_to(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "span.btn.btn-outline-warning").click()

    def result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return (result)

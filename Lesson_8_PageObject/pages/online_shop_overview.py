from selenium.webdriver.common.by import By


class OverviewPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def total(self):
        total = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        amount = total.split(": ")[1]
        return (amount)

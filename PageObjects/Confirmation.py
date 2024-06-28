from selenium.webdriver.common.by import By


class Confirmation:

    def __init__(self, driver):
        self.driver = driver

    itemincart = (By.XPATH, "//button[@class='btn btn-success']")

    def cart(self):
        return self.driver.find_element(*Confirmation.itemincart)
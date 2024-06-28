from selenium.webdriver.common.by import By


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver
    countryselect = (By.ID, "country")
    confirmindia = (By.LINK_TEXT, "India")
    checkboxclick = (By.ID, "checkbox2")
    checkboxclick1 = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitbut = (By.XPATH, "//input[@type='submit']")
    successful = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def countryname(self):
        return self.driver.find_element(*PurchasePage.countryselect)

    def selectindia(self):
        return self.driver.find_element(*PurchasePage.confirmindia)

    def checkbox(self):
        return self.driver.find_element(*PurchasePage.checkboxclick)

    def checkboxconfirm(self):
        return self.driver.find_element(*PurchasePage.checkboxclick1)

    def submit(self):
        return self.driver.find_element(*PurchasePage.submitbut)

    def success(self):
        return self.driver.find_element(*PurchasePage.successful)
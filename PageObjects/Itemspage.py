from selenium.webdriver.common.by import By


class ItemsPage:

    def __init__(self, driver):
        self.driver = driver

    itemlists = (By.XPATH, "//app-card-list[@class='row']/app-card/div")
    checkoutbutton = (By.XPATH, "//div[@id='navbarResponsive']/ul/li")

    def listsearch(self):
        return self.driver.find_elements(*ItemsPage.itemlists)

    def checkoutbut(self):
        return self.driver.find_element(*ItemsPage.checkoutbutton)
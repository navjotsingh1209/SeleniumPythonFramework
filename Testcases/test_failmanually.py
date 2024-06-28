from selenium.webdriver.common.by import By
from PageObjects.Confirmation import Confirmation
from PageObjects.HomePage import HomePage
from PageObjects.Itemspage import ItemsPage
from PageObjects.PurchasePage import PurchasePage
from Utilities.BaseClass import BaseClass

#tc1
class Testcases2(BaseClass):

    def test_failmanually(self):

        log = self.getlogging()

        homepage = HomePage(self.driver)    #obj of differnt pages
        itemspage = ItemsPage(self.driver)  #obj of differnt pages
        cartpage = Confirmation(self.driver)    #obj of differnt pages
        purchasepage = PurchasePage(self.driver)    #obj of differnt pages

        homepage.shop().click()
        log.info("Searching the product")
        list1 = itemspage.listsearch()
        count = len(list1)
        assert count > 0

        for phonename in list1:
            prodname = phonename.find_element(By.XPATH, "div/h4").text
            log.info(prodname)
            if prodname == "Blackberry":
                log.info("Blackberry has been selected")
                phonename.find_element(By.XPATH, "div/button").click()

        itemspage.checkoutbut().click()
        cartpage.cart().click()

        purchasepage.countryname().send_keys("ind")
        self.waitwithlink("India")

        purchasepage.selectindia().click()
        if not purchasepage.checkbox().is_selected():
            purchasepage.checkboxconfirm().click()
        purchasepage.submit().click()
        self.waitwithxpath("//div[@class='alert alert-success alert-dismissible']")
        suc = purchasepage.success().text
        assert "Success!" in suc
        log.info("Test Pass")

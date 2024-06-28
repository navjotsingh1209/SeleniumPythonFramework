import pytest
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")

class BaseClass:

    def waitwithlink(self,link):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, link)))

    def waitwithxpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, xpath)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getlogging(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatoflog = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatoflog)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
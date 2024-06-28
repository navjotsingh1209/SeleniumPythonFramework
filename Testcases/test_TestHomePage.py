import pytest

from TestData.HomePageData import HomePageData
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


#tc2
class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["FirstName"])
        homepage.getEmail().send_keys(getData["LastName"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("tc3"))
    def getData(self, request):
        return request.param

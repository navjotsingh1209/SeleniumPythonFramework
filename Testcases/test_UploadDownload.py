import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# tc3
def test_uploadanddownlaod():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    file_path = "C:\\Users\\Navjo\\Desktop\\Selenuim project\\Uploaddownload.xlsx"
    driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
    driver.maximize_window()
    print(driver.title)
    driver.find_element(By.ID, "downloadButton").click()
    time.sleep(5)
    # edit the excel with updated value


time.sleep(3)

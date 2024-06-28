import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="To run it in different browser"
    )

@pytest.fixture(scope ="class")
def setup(request):

    global driver
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

#    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument("headless")  # run without visible chrome
#    chrome_options.add_argument("--ignore-certificate-errors")  # SSL certiofuicate to be ignored

    # attach the chrome_option with browser
#    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    driver.implicitly_wait(5)
    driver.maximize_window()
    print(driver.title)

    request.cls.driver = driver
    yield
    driver.close()





@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)